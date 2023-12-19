#!/usr/bin/env python3
""" Define update_topics """


def update_topics(mongo_collection, name, topics):
    """ Changes all topics of a school document on the name
    Args:
        mongo_collection(Collection): pymongo collection object
        name(string): school name to update
        topics(list): list of topics approached in the school
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
