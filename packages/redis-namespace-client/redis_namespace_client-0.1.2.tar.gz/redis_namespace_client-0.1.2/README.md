# redis-namespace-client

A simple Redis client for Python with support for:

- Namespacing
- JSON serialization
- Expiry (TTL)
- Logging
- `.env` support via `python-dotenv`

## Installation

```bash
pip install redis-namespace-client
````

## Usage

```python
from redis_namespace_client import redis_set, redis_get

# Set a key
redis_set("mykey", {"foo": "bar"}, ex=3600)

# Get the key
value = redis_get("mykey")
print(value)
```

## Environment Variables

Create a `.env` file or export these:

```env
REDIS_ERP_HOST=localhost
REDIS_ERP_PORT=6379
REDIS_ERP_DB=3
REDIS_ERP_NAMESPACE=my_namespace
```

````

Enjoy
[![PyPI version](https://badge.fury.io/py/redis-namespace-client.svg)](https://pypi.org/project/redis-namespace-client/)