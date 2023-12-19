#!/usr/bin/env python3
""" Define schools_by_topic """


def schools_by_topic(mongo_collection, topic):
    """ Returns the list of school having specific topic """
    return mongo_collection.find({"topics": topic})
