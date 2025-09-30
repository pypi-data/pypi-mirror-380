# ZenX
ZenX is a opinionated framework for building highly efficient and performant web scrapers in python.


## Install

```bash
pip install zenx
```


## Cli commands

```bash
zenx startproject <project_name> # start a new zenx project
zenx list # list all available spiders and pipelines in the created project

zenx crawl <spider_name> # run a spider
zenx crawl <spider_name> <spider_name> # run multiple spiders
zenx crawl all # run all spiders in a zenx project

zenx crawl <spider_name> --forever # run spider continuously
zenx crawl all --exclude <spider_name> # run all spiders in a zenx project except the excluded one

zenx runspider <spider_file> # run a spider from a file

zenx --help # show all commands
```

## Project structure

```
project_root/
├── spiders/
│   ├── __init__.py
│   ├── spider1.py
│   └── spider2.py
└── zenx.toml
```

## Config

```python

APP_ENV = "dev"
ZENX_VERSION = "0.1.0"
LOG_LEVEL = "DEBUG"

SESSION_BACKEND = "memory" # memory, redis
# in case of redis session backend, SESSION_BLUEPRINT_REDIS_KEY is required
SESSION_BLUEPRINT_REDIS_KEY = "blueprint:123"

SESSION_POOL_SIZE = 10 # number of sessions to keep in the pool
SESSION_AGE = 600 # session age in seconds
ACCESS_DENIAL_STATUS_CODES = [401, 403, 429] # status codes to consider as access denial and expire the session

CONCURRENCY = 1 # number of tasks to run concurrently
TASK_INTERVAL_SECONDS = 1.0 # interval between tasks in seconds
START_OFFSET_SECONDS = 60.0 # offset to start the tasks at

MAX_SCRAPE_DELAY = 0.0 # max scrape delay in seconds, disabled by default, older posts will be dropped

DB_TYPE = "memory" # memory, redis, sqlite
DB_NAME = "zenx" # database name
DB_USER = "zenx" # database user
DB_PASS = "zenx" # database password
DB_HOST = "localhost" # database host
DB_PORT = 6379 # database port
DB_PATH = ".zenx/data.db" # database path
DQ_MAX_SIZE = 1000 # max size of the deque for memory database
REDIS_RECORD_EXPIRY_SECONDS = 3456000 # redis record expiry in seconds

PROXY = "http://localhost:8080" # proxy to use

SYNOPTIC_GRPC_SERVER_URI = "ingress.opticfeeds.com"
SYNOPTIC_GRPC_TOKEN = "123"
SYNOPTIC_GRPC_ID = "123"

SYNOPTIC_ENTERPRISE_USEAST1_GRPC_SERVER_URI = "us-east-1.enterprise.synoptic.com:50051"
SYNOPTIC_ENTERPRISE_EUCENTRAL1_GRPC_SERVER_URI = "eu-central-1.enterprise.synoptic.com:50051"
SYNOPTIC_ENTERPRISE_EUWEST2_GRPC_SERVER_URI = "eu-west-2.enterprise.synoptic.com:50051"
SYNOPTIC_ENTERPRISE_USEAST1CHI2A_GRPC_SERVER_URI = "us-east-1-chi-2a.enterprise.synoptic.com:50051"
SYNOPTIC_ENTERPRISE_USEAST1NYC2A_GRPC_SERVER_URI = "us-east-1-nyc-2a.enterprise.synoptic.com:50051"
SYNOPTIC_ENTERPRISE_APNORTHEAST1_GRPC_SERVER_URI = "ap-northeast-1.enterprise.synoptic.com:50051"
SYNOPTIC_ENTERPRISE_GRPC_TOKEN = "123"
SYNOPTIC_ENTERPRISE_GRPC_ID = "123"

SYNOPTIC_DISCORD_WEBHOOK = "https://discord.com/api/webhooks/123"

SYNOPTIC_WS_API_KEY = "123"
SYNOPTIC_WS_STREAM_ID = "123"
SYNOPTIC_FREE_WS_API_KEY = "123"
SYNOPTIC_FREE_WS_STREAM_ID = "123"

ITXP_SOCKET_PATH = "/tmp/itxpmonitor.sock" # itxp socket path for itxp pipeline

MONITOR_ITXP_SOCKET_PATH = "/tmp/itxpmonitor.sock" # itxp socket path for itxp monitor
MONITOR_ITXP_TRIGGER_STATUS_CODE = 200 # itxp trigger status code
MONITORING_ENABLED = True 

SOLVER_SERVICE_API_URL = "http://localhost:8000" 
SOLVER_SERVICE_API_KEY = "123" 
SOLVER_TASK_CHECK_INTERVAL = 5 
SOLVER_TRACK_INTERVAL = 2
SOLVER_LOG_INTERVAL = 60
SOLVER_SPARE_BLUEPRINTS = 0 # spare blueprints to have in redis ready to be used

```


## example zenx project from scratch

```bash
mkdir tutorial
cd tutorial

# create virtual environment
python -m venv .venv
source .venv/bin/activate

# install zenx
pip install zenx

zenx startproject tutorial # create a new zenx project
✅ Project 'tutorial' created successfully.

.
├── tutorial
│   └── spiders
│       └── __init__.py
└── zenx.toml

```


## create a new spider
tutorial/spiders/books_spider.py
```python

from typing import Dict, List
from zenx.http import Response
from zenx.spiders import Spider


class BooksSpider(Spider):
    name = "books"
    client_name = "curl_cffi"


    def parse(self, response: Response) -> List[Dict]:
        items = []

        books = response.xpath("//article[@class='product_pod']")
        for book in books:
            title = book.xpath(".//h3/a/@title").get()
            price = book.xpath(".//p[@class='price_color']/text()").get()
            link = book.xpath(".//h3/a/@href").get()
            item = {
                "_id": link,
                "title": title,
                "price": price
            }
            items.append(item)

        return items


    async def process_response(self, response: Response) -> None:
        if response.status != 200:
            return
        items = self.parse(response)
        for item in items:
            self.create_task(self.pm.process_item(item, self.name))


    async def crawl(self):
        url = "https://books.toscrape.com/"
        response = await self.request(url)
        await self.process_response(response)
```



