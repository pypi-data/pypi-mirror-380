import asyncio
import time
from typing import Callable, List, Coroutine
import pebble
from structlog import BoundLogger
import uvloop
import setproctitle

from zenx.exceptions import NoBlueprintAvailable, NoSessionAvailable
from zenx.listeners import Listener
from zenx.logger import configure_logger
from zenx.monitors import Monitor
from zenx.pipelines import PipelineManager
from zenx.database import DBClient
from zenx.http import HttpClient
from zenx.spiders import Spider
from zenx.settings import Settings, settings as global_settings


class Engine:


    def __init__(self, forever: bool) -> None:
        self.forever = forever


    async def _schedule_task(self, t_func: Callable[[], Coroutine], start_time: float, logger: BoundLogger, settings: Settings) -> None:
        """ Run task at fixed interval or ASAP """
        if settings.TASK_INTERVAL_SECONDS > 0:
            loop = asyncio.get_running_loop()
            while True:
                logger.debug("scheduled", start_time=start_time)
                # loop.time works like a stopwatch, how much time has passed since the start of the program
                delay = start_time - loop.time()
                if delay > 0:
                    await asyncio.sleep(delay)

                try:
                    await t_func()
                except (NoSessionAvailable, NoBlueprintAvailable):
                    logger.error("failed", task="crawl")
                except Exception:
                    logger.exception("failed", task="crawl")

                start_time += settings.TASK_INTERVAL_SECONDS
        else: # run immediately
            while True:
                try:
                    await t_func()
                except Exception:
                    logger.exception("failed", task="crawl")


    async def _execute_spider(self, spider_name: str, settings: Settings) -> None:
        spider_cls = Spider.get_spider(spider_name)
        for name, value in spider_cls.custom_settings.items():
            setattr(settings, name, value)
        logger = configure_logger(spider_cls.name, settings)

        if settings.APP_ENV == "dev":
            logger.warning("dev", pipelines=spider_cls.pipelines[:1], db="memory", monitor=None, spider=spider_name)
            spider_cls.pipelines = ["preprocess"]
            spider_cls.monitor_name = None

        db = DBClient.get_db(settings.DB_TYPE)(logger=logger, settings=settings)
        await db.open()

        client = HttpClient.get_client(spider_cls.client_name)(logger=logger, db=db, settings=settings) # type: ignore[call-arg]
        # await client.open()
        
        if settings.MONITORING_ENABLED:
            # this pipeline is only intended for providing data to itxp monitor
            spider_cls.pipelines.append("itxp") 
        pm = PipelineManager(
            pipeline_names=spider_cls.pipelines,
            logger=logger,
            db=db,
            settings=settings
        )
        await pm.open_pipelines()

        if not settings.MONITORING_ENABLED:
            spider_cls.monitor_name = None
        monitor = Monitor.get_monitor(spider_cls.monitor_name)(logger=logger, settings=settings) if spider_cls.monitor_name else None
        if monitor:
            await monitor.open()

        spider = spider_cls(client=client, pm=pm, logger=logger, settings=settings, monitor=monitor)
        await spider.open()
        # First, run spider's open. This allows the spider to configure the client
        # before the client's connection pool is initialized.
        await client.open()
        try:
            loop = asyncio.get_running_loop()
            if self.forever:
                # 28306550 * 60 + 10.0 = 1698393010.0 (real world time in future)
                wall_clock_start_time = int(time.time() / 60) * 60 + settings.START_OFFSET_SECONDS
                # loop.time works like a stopwatch, how much time has passed since the start of the program
                # program has been running for 5.2 seconds, loop.time will return 5.2
                # 1698393005.5 - 5.2 = 1698393000.3
                clock_offset = time.time() - loop.time()
                # 1698393010.0 - 1698393000.3 = 9.7 so _schedule_task will be called when stopwatch (loop.time) reaches 9.7 seconds
                start_time = wall_clock_start_time - clock_offset

                stagger_seconds = settings.TASK_INTERVAL_SECONDS / settings.CONCURRENCY
                async with asyncio.TaskGroup() as tg:
                    for i in range(settings.CONCURRENCY):
                        task_start_time = start_time + (i * stagger_seconds)
                        tg.create_task(self._schedule_task(spider.crawl, task_start_time, logger, settings))
            else:
                await spider.crawl()
        except asyncio.CancelledError: # main func (_execute_spider) raises CancelledError instead of KeyboardInterrupt on ctrl+c
            logger.debug("cancelled", task="crawl", spider=spider_name)
        finally:
            logger.info("shutdown", spider=spider_name)
            logger.debug("waiting", background_tasks=len(spider.background_tasks), belong_to="spider", spider=spider_name)
            while spider.background_tasks:
                for t in list(spider.background_tasks):
                    # tasks that are long-running e.g someting inside loop
                    if "cancellable" in t.get_name():
                        t.cancel()
                await asyncio.gather(*spider.background_tasks, return_exceptions=True)
            await spider.close()
            await client.close()
            await db.close()
            if monitor:
                await monitor.close()
            await pm.close_pipelines()


    def run_spider(self, spider: str) -> None:
        setproctitle.setproctitle(f"zenx-{global_settings.ZENX_VERSION}:{spider}")
        settings = global_settings.model_copy()
        uvloop.run(self._execute_spider(spider, settings))


    def run_spiders(self, spiders: List[str]) -> None:
        with pebble.ProcessPool(max_workers=len(spiders)) as pool:
            for spider in spiders:
                pool.schedule(self.run_spider, [spider])


    async def _execute_listener(self, listener_name: str, settings: Settings) -> None:
        listener_cls = Listener.get_listener(listener_name)
        for name, value in listener_cls.custom_settings.items():
            setattr(settings, name, value)
        logger = configure_logger(listener_cls.name, settings)

        if settings.APP_ENV == "dev":
            logger.warning("dev",  pipelines=listener_cls.pipelines[:1], db="memory", monitor=None, listener=listener_name)
            listener_cls.pipelines = ["preprocess"]
            listener_cls.monitor_name = None

        db = DBClient.get_db(settings.DB_TYPE)(logger=logger, settings=settings)
        await db.open()

        pm = PipelineManager(
            pipeline_names=listener_cls.pipelines,
            logger=logger,
            db=db,
            settings=settings
        )
        await pm.open_pipelines()

        monitor = Monitor.get_monitor(listener_cls.monitor_name)(logger=logger, settings=settings) if listener_cls.monitor_name else None
        if monitor:
            await monitor.open()

        listener = listener_cls(pm=pm, logger=logger, settings=settings, monitor=monitor)
        listen_task = asyncio.create_task(listener.listen())
        try:
            await listen_task
        except asyncio.CancelledError: # main func (_execute_listener) raises CancelledError instead of KeyboardInterrupt on ctrl+c
            logger.debug("cancelled", task="listen", listener=listener_name)
            listen_task.cancel()
        except Exception: # task terminated on exception inside
            logger.exception("failed", task="listen", listener=listener_name)
        finally:
            logger.info("shutdown", listener=listener_name)
            logger.debug("waiting", background_tasks=len(listener.background_tasks), belong_to="listener", listener=listener_name)
            while listener.background_tasks:
                for t in list(listener.background_tasks):
                    # tasks that are long-running e.g someting inside loop
                    if "cancellable" in t.get_name():
                        t.cancel()
                await asyncio.gather(*listener.background_tasks, return_exceptions=True)
            await db.close()
            if monitor:
                await monitor.close()
            await pm.close_pipelines()


    def run_listener(self, listener: str) -> None:
        setproctitle.setproctitle(f"zenx-{global_settings.ZENX_VERSION}:{listener}")
        settings = global_settings.model_copy()
        uvloop.run(self._execute_listener(listener, settings))
