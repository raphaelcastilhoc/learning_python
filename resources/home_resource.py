from flask import Flask
from flask_restful import Resource, Api

class HomeResource(Resource):
    def get(self):
        message = "Hello World"
        return message