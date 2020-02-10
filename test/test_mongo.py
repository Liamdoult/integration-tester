import pymongo 
import pytest

from integration_tester import mongo


def test_mongo():
    """ Standard mongodb test. """
    database = mongo.MongoDB()
    database.wait_until_ready()
    
    db = pymongo.MongoClient().test
    collection = db.test
    collection.insert_one({"test": "test"})
    assert list(collection.find({}))

    database.reset()
    assert not list(collection.find({}))

    del(database)

