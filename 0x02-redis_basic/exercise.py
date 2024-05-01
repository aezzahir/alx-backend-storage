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
