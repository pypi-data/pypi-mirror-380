""" 
Responsible for managing blueprint lifecycles:
- Fetches new blueprints from the solver service as needed.
- Stores retrieved blueprints in the database.
- Monitors blueprint availability and automatically requests additional blueprints when supply is low.
"""
import asyncio
from typing import Dict, Set
from structlog import BoundLogger
import redis.asyncio as redis
import httpx

from zenx.settings import Settings



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
    

    async def check_task_status(self, task_id: str) -> None:
        url = f"{self.settings.SOLVER_SERVICE_API_URL}/tasks/{task_id}"
        try:
            response = await self.client.get(url)
            if response.status_code == 200:
                self.pending_tasks.remove(task_id)
                self.logger.info("completed", task_id=task_id)
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
                for task_id in self.pending_tasks:
                    tg.create_task(self.check_task_status(task_id))
            await asyncio.sleep(self.settings.SOLVER_TASK_CHECK_INTERVAL)


    async def submit_challenge(self, url: str, challenge: str, spider: str) -> None:
        try:
            response = await self.client.post(f"{self.settings.SOLVER_SERVICE_API_URL}/solve", json={
                "url": url,
                "challenge": challenge,
                "spider": spider
            })
            if response.status_code != 201:
                raise Exception(f"unexpected response: {response.status_code}")
            task_id = response.json()["task_id"]
            self.pending_tasks.add(task_id)
            self.logger.debug("submitted", task_id=task_id, challenge=challenge, spider=spider)
        except Exception as e:
            self.logger.error("submitting", exception=str(e), challenge=challenge, spider=spider)
    

    async def track_blueprints(self, target: Dict) -> None:
        self.logger.debug("tracking blueprints")

        redis_key = f"{target['challenge']}:{target["spider"]}"
        while True:
            size = await self.r.llen(redis_key)
            self.logger.info("available", size=size, redis_key=redis_key)

            if size < self.settings.SESSION_POOL_SIZE and not self.pending_tasks:
                required_count = self.settings.SESSION_POOL_SIZE - size
                async with asyncio.TaskGroup() as tg:
                    for _ in range(required_count):
                        tg.create_task(self.submit_challenge(target["url"], target["challenge"], target["spider"]))
                self.logger.info("requested", count=required_count, challenge=target['challenge'], spider=target['spider'])

            await asyncio.sleep(self.settings.SOLVER_TRACK_INTERVAL)


    async def run(self) -> None:
        async with asyncio.TaskGroup() as tg:
            for target in self.settings.SOLVER_TARGETS:
                tg.create_task(self.track_blueprints(target))
            tg.create_task(self.track_pending_tasks())
