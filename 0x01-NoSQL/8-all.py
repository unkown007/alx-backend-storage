#!/usr/bin/env python3
""" Define list_all """


def list_all(mongo_collection):
    """ Lists all documents in a collection
    Args:
        mongo_collection(Collection): MongoDB School Collection
    Return: A Cursor containing all elements
    """
    return mongo_collection.find()
