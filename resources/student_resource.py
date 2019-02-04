from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from models.student import Student

class StudentResource(Resource):
    @jwt_required()
    def get(self, name):
        student = Student.get_by_name(name)
        return student, 200 if student else 402

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('price', type=float, required=True, help='This field is required!')
        data = parser.parse_args()

        student = Student.add(name);
        return student, 201 if student else 400
