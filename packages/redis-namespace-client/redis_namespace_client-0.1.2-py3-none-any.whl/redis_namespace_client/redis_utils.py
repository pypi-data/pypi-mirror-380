import redis
import os
from dotenv import load_dotenv
import json
import logging

# Load environment variables
load_dotenv()

# Redis config (env-driven)
REDIS_HOST = os.getenv("REDIS_ERP_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_ERP_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_ERP_DB", 3))
REDIS_NAMESPACE = os.getenv("REDIS_ERP_NAMESPACE", "zoho_odoo_middleware")

# Initialize Redis client
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

# Configure logging
logging.basicConfig(level=logging.INFO)

def _ns_key(key: str) -> str:
    """Applies the namespace prefix to a Redis key."""
    return f"{REDIS_NAMESPACE}:{key}"

def redis_set(key: str, value, ex=None):
    """
    Set a key with JSON-encoded value and optional expiration.

    Args:
        key (str): Key name.
        value (Any): JSON-serializable value.
        ex (int, optional): Expiry time in seconds.
    """
    namespaced_key = _ns_key(key)
    try:
        redis_client.set(namespaced_key, json.dumps(value), ex=ex)
        logging.info(f"Set Redis key: {namespaced_key}")
    except Exception as e:
        logging.error(f"Error setting Redis key {namespaced_key}: {e}")

def redis_get(key: str):
    """
    Get a JSON-decoded value from Redis.

    Args:
        key (str): Key name.

    Returns:
        Any or None: Decoded value, or None if key doesn't exist or fails.
    """
    namespaced_key = _ns_key(key)
    try:
        val = redis_client.get(namespaced_key)
        if val:
            logging.info(f"Retrieved Redis key: {namespaced_key}")
            return json.loads(val)
    except Exception as e:
        logging.error(f"Error getting Redis key {namespaced_key}: {e}")
    return None

def redis_delete(key: str):
    """Delete a key from Redis."""
    namespaced_key = _ns_key(key)
    try:
        redis_client.delete(namespaced_key)
        logging.info(f"Deleted Redis key: {namespaced_key}")
    except Exception as e:
        logging.error(f"Error deleting Redis key {namespaced_key}: {e}")

def redis_key_exists(key: str) -> bool:
    """Check if a namespaced key exists in Redis."""
    namespaced_key = _ns_key(key)
    try:
        return bool(redis_client.exists(namespaced_key))
    except Exception as e:
        logging.error(f"Error checking Redis key {namespaced_key}: {e}")
        return False

def list_all_keys():
    """List all keys in the current Redis namespace."""
    try:
        keys = redis_client.keys(f"{REDIS_NAMESPACE}:*")
        return [key.decode("utf-8") for key in keys]
    except Exception as e:
        logging.error(f"Error listing Redis keys: {e}")
        return []
