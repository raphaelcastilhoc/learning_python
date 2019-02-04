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
        item = next(filter(lambda x: x['name'] == name, students), None)
        if item:
            return None

        student = {"name": name}
        students.append(student)
        return student
