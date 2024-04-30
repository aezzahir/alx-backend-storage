#!/usr/bin/env python3
""" Mongo With python """


def schools_by_topic(mongo_collection, topic):
    """ Returns the list of school having a specific topic """
    documents = mongo_collection.find({"topics": topic})
    return list(documents)