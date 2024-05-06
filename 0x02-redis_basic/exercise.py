#!/usr/bin/env python3
""" Module define and implements Cache class
"""
from typing import Union
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
