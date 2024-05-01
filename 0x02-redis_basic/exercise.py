#!/usr/bin/env python3
"""
This Module handles cache ....
"""
from typing import Callable, Optional, Union
import redis
from uuid import uuid4


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
