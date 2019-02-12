from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from models.robot import Robot

class RobotApi(Resource):
    @jwt_required()
    def get(self, robot_id):
        robot = Robot.get_by_id(robot_id)
        parsed_robot = Robot(robot['name']).json()

        return parsed_robot, 200 if parsed_robot else 402

    @jwt_required()
    def delete(self, robot_id):
        Robot.delete(robot_id)
        return 200

class RobotListApi(Resource):
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