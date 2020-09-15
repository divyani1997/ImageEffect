from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from Cartoon import cartoon
from Skecth import sketch

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
api.add_resource(sketch, '/sketch', endpoint='sketch')
api.add_resource(sketch, '/negative', endpoint='negative')

# @app.route('/')
# def hello_world():
#    return 'hello test'


if __name__ == '__main__':
    app.run(debug=True)