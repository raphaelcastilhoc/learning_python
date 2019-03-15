from flask import Flask, request
# from flask_restful import Resource, Api, reqparse
# from flask_jwt import JWT, jwt_required
# from security import authenticate, identity
# from resources.student_resource import StudentResource
# from resources.home_resource import HomeResource
# from resources.robot_resource import RobotApi, RobotListApi

app = Flask(__name__)
# app.secret_key = 'raphael'
# api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# jwt = JWT(app, authenticate, identity)

# api.add_resource(HomeResource, '/')
# api.add_resource(StudentResource, '/student/<string:name>')
# api.add_resource(RobotApi, '/robot/<string:robot_id>')
# api.add_resource(RobotListApi, '/robots/')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
