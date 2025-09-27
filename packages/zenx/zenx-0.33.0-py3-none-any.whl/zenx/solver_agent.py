""" 
Responsible for managing blueprint lifecycles:
- Fetches new blueprints from the solver service as needed.
- Stores retrieved blueprints in the database.
- Monitors blueprint availability and automatically requests additional blueprints when supply is low.
"""
import asyncio
from typing import Dict, Set, List
from structlog import BoundLogger
import redis.asyncio as redis
import httpx

from zenx.settings import Settings
from zenx.spiders import Spider



class SolverAgent():
    name = "solver_agent"
    pending_tasks: Dict[str, Set[str]] = {}

    
    def __init__(self, logger: BoundLogger, settings: Settings) -> None:
        if not settings.SOLVER_SERVICE_API_KEY:
            raise ValueError("missing SOLVER_SERVICE_API_KEY")
        if not settings.SOLVER_SERVICE_API_URL:
            raise ValueError("missing SOLVER_SERVICE_API_URL")
        self.logger = logger
        self.settings = settings
        self.api_key = settings.SOLVER_SERVICE_API_KEY
        self.api_url = settings.SOLVER_SERVICE_API_URL.rstrip("/")
        self.r = redis.Redis(
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            password=settings.DB_PASS,
            decode_responses=True,
        )
        self.client = httpx.AsyncClient(headers={"x-api-key": self.api_key})
    

    async def check_task_status(self, task_id: str, key: str) -> None:
        url = f"{self.api_url}/tasks/{task_id}"
        try:
            response = await self.client.get(url)
            if response.status_code == 200:
                self.pending_tasks[key].remove(task_id)
                self.logger.info("completed", task_id=task_id)
                session = response.json()['session']
                await self.r.lpush(key, session)
            elif response.status_code == 202:
                self.logger.debug("pending", task_id=task_id)
            else:
                raise Exception(f"unexpected response: {response.status_code}")
        except Exception as e:
            self.logger.error("checking", exception=str(e))


    async def track_pending_tasks(self) -> None:
        self.logger.debug("tracking pending tasks")
        while True:
            async with asyncio.TaskGroup() as tg:
                for key, tasks in self.pending_tasks.items():
                    for task_id in tasks:
                        tg.create_task(self.check_task_status(task_id, key))
            await asyncio.sleep(self.settings.SOLVER_TASK_CHECK_INTERVAL)


    async def submit_challenge(self, url: str, challenge: str, proxy: str, spider: str) -> None:
        try:
            response = await self.client.post(f"{self.api_url}/solve", json={
                "url": url,
                "challenge": challenge,
                "proxy": proxy,
                "spider": spider
            })
            if response.status_code != 201:
                raise Exception(f"unexpected response: {response.status_code}")
            task_id = response.json()["task_id"]
            key = f"{challenge}:{spider}"
            if key not in self.pending_tasks:
                self.pending_tasks[key] = set()
            self.pending_tasks[key].add(task_id)
            self.logger.debug("submitted", task_id=task_id, challenge=challenge, spider=spider)
        except Exception as e:
            self.logger.error("submitting", exception=str(e), challenge=challenge, spider=spider)
    

    async def track_blueprints(self, target: Dict) -> None:
        self.logger.debug("tracking", target=target)

        redis_key = f"{target['challenge']}:{target["spider"]}"
        while True:
            size = await self.r.llen(redis_key)
            self.logger.info("available", size=size, redis_key=redis_key)

            if size < self.settings.SESSION_POOL_SIZE and not self.pending_tasks:
                required_count = self.settings.SESSION_POOL_SIZE - size
                async with asyncio.TaskGroup() as tg:
                    for _ in range(required_count):
                        tg.create_task(self.submit_challenge(target["url"], target["challenge"], target['proxy'], target["spider"]))
                self.logger.info("requested", count=required_count, challenge=target['challenge'], spider=target['spider'])

            await asyncio.sleep(self.settings.SOLVER_TRACK_INTERVAL)


    def collect_targets(self) -> List[Dict]:
        targets = []
        for spider in Spider.spider_list():
            spider_cls = Spider.get_spider(spider)
            blueprint_key = spider_cls.custom_settings.get("SESSION_BLUEPRINT_REDIS_KEY")
            if not blueprint_key:
                continue
            challenge_url = spider_cls.custom_settings.get("CHALLENGE_URL")
            proxy = spider_cls.custom_settings.get("PROXY")
            target = {
                "url": challenge_url,
                "challenge": blueprint_key.split(":")[0],
                "proxy": proxy,
                "spider": spider,
            }
            targets.append(target)
        self.logger.info("collected", targets=targets)
        return targets


    async def run(self) -> None:
        targets = self.collect_targets() 
        async with asyncio.TaskGroup() as tg:
            for target in targets:
                tg.create_task(self.track_blueprints(target))
            tg.create_task(self.track_pending_tasks())



