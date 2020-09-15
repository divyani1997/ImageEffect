from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from Cartoon import cartoon

app = Flask(__name__)

api = Api(app)


class Hello(Resource):
    def get(self):
        return jsonify({'message': 'hello world'})

    def post(self):
        data = request.get_json()
        return data


api.add_resource(Hello, '/hi')
api.add_resource(cartoon, '/cartoonify')

# @app.route('/')
# def hello_world():
#    return 'hello test'


if __name__ == '__main__':
    app.run(debug=True)