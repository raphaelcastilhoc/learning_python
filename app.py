from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from resources.student_resource import StudentResource

app = Flask(__name__)
app.secret_key = 'raphael'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(StudentResource, '/student/<string:name>')

app.run(port=5000, debug=True)
