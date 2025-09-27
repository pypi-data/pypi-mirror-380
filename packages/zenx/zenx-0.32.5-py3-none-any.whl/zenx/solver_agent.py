""" 
Responsible for managing blueprint lifecycles:
- Fetches new blueprints from the solver service as needed.
- Stores retrieved blueprints in the database.
- Monitors blueprint availability and automatically requests additional blueprints when supply is low.
"""

import asyncio
from typing import Set
from structlog import BoundLogger
import redis.asyncio as redis
import httpx

from zenx.settings import Settings
from zenx.spiders.base import Spider


class SolverAgent():
    name = "solver_agent"
    pending_tasks: Set[str] = set()

    
    def __init__(self, logger: BoundLogger, settings: Settings) -> None:
        self.logger = logger
        self.settings = settings
        self.r = redis.Redis(
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            password=settings.DB_PASS,
            decode_responses=True,
        )
        self.client = httpx.AsyncClient(headers={"x-api-key": settings.SOLVER_SERVICE_API_KEY})
    
    
    async def track_blueprints(self, redis_key: str) -> None:
        while True:
            size = await self.r.llen(redis_key)
            self.logger.info("blueprints", size=size, redis_key=redis_key)
            if size < self.settings.SESSION_POOL_SIZE and not self.tasks:
                ...
            await asyncio.sleep(2)


    async def remove_pending_task(self, task: asyncio.Task) -> None:
        try:
            result = task.result()
            if result.status_code == 200:
                self.pending_tasks.remove(task.get_name())
        except Exception:
            pass


    async def track_pending_tasks(self) -> None:
        while True:
            tasks = []
            async with asyncio.TaskGroup() as tg:
                for task_id in self.pending_tasks:
                    url = f"{self.settings.SOLVER_SERVICE_API_URL}/tasks/{task_id}"
                    task = tg.create_task(self.client.get(url), name=task_id)
                    task.add_done_callback(self.remove_pending_task)
                    tasks.append(task)
            await asyncio.gather(*tasks)
            await asyncio.sleep(5)


    async def solve_challenge(self, url: str, challenge: str, spider: str) -> None:
        response = await self.client.post(f"{self.settings.SOLVER_SERVICE_API_URL}/solve", json={
            "url": url,
            "challenge": challenge,
            "spider": spider
        })
        if response.status_code == 201:
            task_id = response.json()["task_id"]
            self.pending_tasks.add(task_id)
        else:
            self.logger.error("request_blueprint", status=response.status_code, response=response.json())
    


    async def collect_spiders_with_challenge(self) -> None:
        # discover the spiders available in the project and read their custom_settings
        # if there is a setting named `SESSION_BLUEPRINT_REDIS_KEY` add it to the list of spiders with challenge
        # if there is no setting named `SESSION_BLUEPRINT_REDIS_KEY` add it to the list of spiders without challenge
        # return the list of spiders with challenge
        # return the list of spiders without challenge
        spiders = []
        for spider in Spider.spider_list():
            spider_cls = Spider.get_spider(spider)
            if spider_cls.custom_settings.get("SESSION_BLUEPRINT_REDIS_KEY"):
                spiders.append(spider)
        self.logger.info("spiders_with_challenge", spiders=spiders)
        return spiders

    
    async def run(self) -> None:
        await self.collect_spiders_with_challenge()