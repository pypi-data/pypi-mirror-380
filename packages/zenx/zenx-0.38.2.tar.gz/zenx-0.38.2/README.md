# ZenX

An opinionated framework for building highly efficient and performant web scrapers in Python.

## Installation

```bash
pip install zenx
```

## CLI Commands

### Project Management
```bash
zenx startproject <project_name>  # Create a new ZenX project
zenx list                          # List all available spiders and pipelines
```

### Running Spiders
```bash
zenx crawl <spider_name>                         # Run a single spider
zenx crawl <spider_name> <spider_name>          # Run multiple spiders
zenx crawl all                                   # Run all spiders
zenx crawl <spider_name> --forever              # Run spider continuously
zenx crawl all --exclude <spider_name>          # Run all except excluded spider
zenx runspider <spider_file>                    # Run spider from a file
```

### Help
```bash
zenx --help  # Show all available commands
```


## Quick Start Example

### 1. Create a New Project

```bash
mkdir tutorial
cd tutorial

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install ZenX
pip install zenx

# Create a new ZenX project
zenx startproject tutorial
```

```
tutorial/
├── spiders/
│   ├── __init__.py
└── zenx.toml
```


### 2. Create a Spider

Create `tutorial/spiders/books_spider.py`:

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
                "_id": link,  # Required field
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
            self.create_task(self.process_item(item, self.name))

    
    # entrypoint
    async def crawl(self):
        url = "https://books.toscrape.com/"
        response = await self.request(url)
        await self.process_response(response)
```

### 3. Run the Spider

```bash
zenx crawl books
```

## Configuration

Configuration options in `zenx.toml`:

### Application Settings
```python
APP_ENV = "dev"
ZENX_VERSION = "0.1.0"
LOG_LEVEL = "DEBUG"
```

### Session Management
```python
SESSION_BACKEND = "memory"  # Options: memory, redis
SESSION_BLUEPRINT_REDIS_KEY = "blueprint:123"  # Required for redis backend
SESSION_POOL_SIZE = 10
SESSION_AGE = 600  # seconds
ACCESS_DENIAL_STATUS_CODES = [401, 403, 429]
```

### Task Execution
```python
CONCURRENCY = 1  # Concurrent tasks
TASK_INTERVAL_SECONDS = 1.0
START_OFFSET_SECONDS = 60.0
MAX_SCRAPE_DELAY = 0.0  # Disabled by default
```

### Database
```python
DB_TYPE = "memory"  # Options: memory, redis, sqlite
DB_NAME = "zenx"
DB_USER = "zenx"
DB_PASS = "zenx"
DB_HOST = "localhost"
DB_PORT = 6379
DB_PATH = ".zenx/data.db"
DQ_MAX_SIZE = 1000
REDIS_RECORD_EXPIRY_SECONDS = 3456000
```

### Network
```python
PROXY = "http://localhost:8080"
```

### Synoptic Integration
```python
SYNOPTIC_GRPC_SERVER_URI = "ingress.opticfeeds.com"
SYNOPTIC_GRPC_TOKEN = "123"
SYNOPTIC_GRPC_ID = "123"

# Enterprise endpoints
SYNOPTIC_ENTERPRISE_USEAST1_GRPC_SERVER_URI = "us-east-1.enterprise.synoptic.com:50051"
SYNOPTIC_ENTERPRISE_EUCENTRAL1_GRPC_SERVER_URI = "eu-central-1.enterprise.synoptic.com:50051"
SYNOPTIC_ENTERPRISE_EUWEST2_GRPC_SERVER_URI = "eu-west-2.enterprise.synoptic.com:50051"
SYNOPTIC_ENTERPRISE_USEAST1CHI2A_GRPC_SERVER_URI = "us-east-1-chi-2a.enterprise.synoptic.com:50051"
SYNOPTIC_ENTERPRISE_USEAST1NYC2A_GRPC_SERVER_URI = "us-east-1-nyc-2a.enterprise.synoptic.com:50051"
SYNOPTIC_ENTERPRISE_APNORTHEAST1_GRPC_SERVER_URI = "ap-northeast-1.enterprise.synoptic.com:50051"
SYNOPTIC_ENTERPRISE_GRPC_TOKEN = "123"
SYNOPTIC_ENTERPRISE_GRPC_ID = "123"

# Discord & WebSocket
SYNOPTIC_DISCORD_WEBHOOK = "https://discord.com/api/webhooks/123"
SYNOPTIC_WS_API_KEY = "123"
SYNOPTIC_WS_STREAM_ID = "123"
SYNOPTIC_FREE_WS_API_KEY = "123"
SYNOPTIC_FREE_WS_STREAM_ID = "123"
```

### Monitoring & ITXP
```python
ITXP_SOCKET_PATH = "/tmp/itxpmonitor.sock"
MONITOR_ITXP_SOCKET_PATH = "/tmp/itxpmonitor.sock"
MONITOR_ITXP_TRIGGER_STATUS_CODE = 200
MONITORING_ENABLED = True
```

### Solver Service
```python
SOLVER_SERVICE_API_URL = "http://localhost:8000"
SOLVER_SERVICE_API_KEY = "123"
SOLVER_TASK_CHECK_INTERVAL = 5
SOLVER_TRACK_INTERVAL = 2
SOLVER_LOG_INTERVAL = 60
SOLVER_SPARE_BLUEPRINTS = 0
```
