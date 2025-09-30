from flask_caching import Cache
from flask import request

from ...config import Config

config = Config("app.cfg")
config.load()
cache_options = {
    "CACHE_" + k.upper(): v for (k, v) in config.get_section("cache", {}).items()
}

cache = Cache(config=cache_options)


def cache_key(*args, **kwargs):
    headers = []
    for key in request.headers.keys():
        if "simdb-" in key.lower():
            headers.append("{}:{}".format(key.lower(), request.headers.get(key, 0)))
    return request.url + "?" + "&".join(headers)


def clear_cache():
    try:
        cache.clear()
    except FileNotFoundError:
        pass  # If /tmp has been cleared by the system then we should ignore this exception
