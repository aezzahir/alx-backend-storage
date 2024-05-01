#!/usr/bin/env python3
"""
This Module handles cache ....
"""
from typing import Callable, Optional, Union
import redis
from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
        Count How many times a method was called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''
            Wrapper function.
        '''
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache(object):

    def __init__(self):
        '''
        Initialize the cache
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            Store data in the cache
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
            Get data from the Cache
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return (value)

    def get_str(self, key: str) -> str:
        '''
            Get a string from the cache.
        '''
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        '''
            Get an int from the cache.
        '''
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
