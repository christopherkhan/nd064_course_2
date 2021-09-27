import json
from flask import Flask, render_template, jsonify, request
from flask_restful import Api, Resource
from services import write_topic

app = Flask(__name__)
api = Api(app)


class Geolocations(Resource):

    def post(self):
        payload = request.get_json()
        result = write_topic(payload)
        return result

api.add_resource(Geolocations, '/geolocations')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({'OK': 'Success'})

if __name__ == "__main__":
    app.run(debug=True)