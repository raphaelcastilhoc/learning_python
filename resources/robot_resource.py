from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from models.robot import Robot

class RobotResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        required=True,
                        help="This fieldis required!"
                        )

    @jwt_required()
    def get(self):
        robots = Robot.get()
        parsed_robots = [Robot(robot['name']).json() for robot in robots]

        return parsed_robots, 200 if parsed_robots else 402

    @jwt_required()
    def post(self):
        robot = self.parser.parse_args()

        robot_id = Robot.add(robot)

        return robot_id, 201 if robot_id else 400