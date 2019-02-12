from pymongo import MongoClient
from bson.objectid import ObjectId

class Robot():
    def __init__(self, name):
        self.name = name

    def json(self):
        return { "name" : self.name }

    @classmethod
    def get_collection(cls):
        client = MongoClient('localhost', 27017)
        database = client.testing_python
        return database.robots

    @classmethod
    def get(cls):
        robots = cls.get_collection().find()
        return robots

    @classmethod
    def get_by_id(cls, robot_id):
        robot = cls.get_collection().find_one({"_id": ObjectId(robot_id)})
        return robot

    @classmethod
    def add(cls, robot):
        robots = cls.get_collection()
        robot_id = robots.insert_one(robot).inserted_id

        return str(robot_id)

    @classmethod
    def delete(cls, robot_id):
        robots = cls.get_collection()
        robots.delete_one({"_id": ObjectId(robot_id)})



