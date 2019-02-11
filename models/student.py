from pymongo import MongoClient

students = []

class Student():

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_by_name(cls, name):
        student = next(filter(lambda x : x["name"] == name, students), None)
        return { "student": student }

    @classmethod
    def add(cls, name):
        client = MongoClient('localhost', 27017)
        database = client.testing_python

        item = next(filter(lambda x: x['name'] == name, students), None)
        if item:
            return None

        student = {"name": name}
        student_colelction = database.students
        student_id = student_colelction.insert_one(student).inserted_id

        return {"student_id": str(student_id)}
