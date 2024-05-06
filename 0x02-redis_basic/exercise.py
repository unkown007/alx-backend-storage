#!/usr/bin/env python3
""" Module define and implements Cache class
"""
from typing import Union, Callable
from uuid import uuid4
import redis


class Cache:
    """ Cache class """

    def __init__(self) -> None:
        """ Initialize the class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates a random key and stores the input data in Redis """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key, fn=None):
        value = self._redis.get(key)
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key):
        """ Get a value in Redis db """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key):
        """ Get a value in Redis db """
        return self.get(key, int)
