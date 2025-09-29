from typing import Dict, List, Literal, Self
from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import find_dotenv
import importlib


class Settings(BaseSettings):
    APP_ENV: str = "dev"
    ZENX_VERSION: str = importlib.metadata.version("zenx")
    LOG_LEVEL: str = "DEBUG"

    SESSION_BACKEND: str = "memory"
    SESSION_POOL_SIZE: int | None = None
    SESSION_AGE: int = 600 # 10 minutes
    SESSION_BLUEPRINT_REDIS_KEY: str | None = None
    ACCESS_DENIAL_STATUS_CODES: List[int] = [401, 403, 429]

    CONCURRENCY: int = 1
    TASK_INTERVAL_SECONDS: float = 1.0
    START_OFFSET_SECONDS: float = 60.0

    MAX_SCRAPE_DELAY: float = 0.0 # disabled

    DB_TYPE: Literal["memory", "redis", "sqlite"] = "memory"
    DB_NAME: str | None = None
    DB_USER: str | None = None
    DB_PASS: str | None = None
    DB_HOST: str | None = "localhost"
    DB_PORT: int | None = 6379
    DB_PATH: str | None = ".zenx/data.db"
    DQ_MAX_SIZE: int = 1000  # max size of the deque for memory database
    REDIS_RECORD_EXPIRY_SECONDS: int = 3456000 # 40 days (40*24*60*60)

    PROXY: str | None = None

    SYNOPTIC_GRPC_SERVER_URI: str = "ingress.opticfeeds.com"
    SYNOPTIC_GRPC_TOKEN: str | None = None
    SYNOPTIC_GRPC_ID: str | None = None
    # enterprise
    SYNOPTIC_ENTERPRISE_USEAST1_GRPC_SERVER_URI: str | None = "us-east-1.enterprise.synoptic.com:50051"
    SYNOPTIC_ENTERPRISE_EUCENTRAL1_GRPC_SERVER_URI: str | None = "eu-central-1.enterprise.synoptic.com:50051"
    SYNOPTIC_ENTERPRISE_EUWEST2_GRPC_SERVER_URI: str | None = "eu-west-2.enterprise.synoptic.com:50051"
    SYNOPTIC_ENTERPRISE_USEAST1CHI2A_GRPC_SERVER_URI: str | None = "us-east-1-chi-2a.enterprise.synoptic.com:50051"
    SYNOPTIC_ENTERPRISE_USEAST1NYC2A_GRPC_SERVER_URI: str | None = "us-east-1-nyc-2a.enterprise.synoptic.com:50051"
    SYNOPTIC_ENTERPRISE_APNORTHEAST1_GRPC_SERVER_URI: str | None = "ap-northeast-1.enterprise.synoptic.com:50051"
    SYNOPTIC_ENTERPRISE_GRPC_TOKEN: str | None = None
    SYNOPTIC_ENTERPRISE_GRPC_ID: str | None = None

    SYNOPTIC_DISCORD_WEBHOOK: str | None = None

    SYNOPTIC_WS_API_KEY: str | None = None
    SYNOPTIC_WS_STREAM_ID: str | None = None
    SYNOPTIC_FREE_WS_API_KEY: str | None = None
    SYNOPTIC_FREE_WS_STREAM_ID: str | None = None

    ITXP_SOCKET_PATH: str | None = "/tmp/itxpmonitor.sock"

    MONITOR_ITXP_SOCKET_PATH: str | None = "/tmp/itxpmonitor.sock"
    MONITOR_ITXP_TRIGGER_STATUS_CODE: int | None = 200
    MONITORING_ENABLED: bool = False

    # SOLVER AGENT
    SOLVER_SERVICE_API_URL: str = "http://localhost:8000"
    SOLVER_SERVICE_API_KEY: str = ""
    SOLVER_TASK_CHECK_INTERVAL: int = 5
    SOLVER_TRACK_INTERVAL: int = 2
    SOLVER_LOG_INTERVAL: int = 10
    SOLVER_SPARE_BLUEPRINTS: int = 0

    model_config = SettingsConfigDict(env_file=find_dotenv(".env"), extra="allow", case_sensitive=True)

    @model_validator(mode="after")
    def model_created(self) -> Self:
        if self.APP_ENV == "dev":
            self.START_OFFSET_SECONDS = 10.0 # can cause issues with the scheduler beacuse scheduler starts at the beginning of the minute, min 60 seconds
            self.DB_TYPE = "memory"
        elif self.APP_ENV == "prod":
            self.MONITORING_ENABLED = True

        if self.SESSION_POOL_SIZE is None:
            self.SESSION_POOL_SIZE = self.CONCURRENCY

        return self

settings = Settings()
