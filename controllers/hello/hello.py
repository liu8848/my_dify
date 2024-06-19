from flask_restful import Resource, marshal_with
from controllers.hello import api


class HelloGetApi(Resource):

    # @api.route('/get')
    def get(self):
        return {
            "message": "Hello World!"
        }


api.add_resource(HelloGetApi, '/get')
