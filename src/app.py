import os
import json
from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from flask_pymongo import PyMongo
from bson import json_util

app = Flask(__name__)

# Install the Flask App and MongoDB instance
mongo_uri = os.environ.get('MONGODB_ENDPOINT')
app.config['MONGO_URI'] = mongo_uri
mongo = PyMongo(app)

# Swagger documentation
SWAGGER_URL = os.environ.get('SWAGGER_URL')
API_URL = os.environ.get('API_URL_PART')
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Flask API'
    }
)
app.register_blueprint(
    swaggerui_blueprint,
    url_prefix=SWAGGER_URL
)

def parse_json(data):
    return json.loads(json_util.dumps(data))

@app.route('/add', methods=['POST'])
def add_key_value():
    data = request.get_json()

    key = data['key']
    if key is None:
        return jsonify({'message': 'Key is required'}, 400)

    value = data['value']
    if value is None:
        return jsonify({'message': 'Value is required'}, 400)

    mongo.db.items.insert_one({'key': key, 'value': value})
    return jsonify({'message': 'Key-value pair added successfully'}, 201)

@app.route('/update', methods=['PUT'])
def update_value():
    data = request.get_json()

    key = data['key']
    if key is None:
        return jsonify({'message': 'Key is required'}, 400)

    new_value = data['new_value']
    if new_value is None:
        return jsonify({'message': 'New value is required'}, 400)

    result = mongo.db.items.update_one({'key': key}, {'$set': {'value': new_value}})
    if result.matched_count == 0:
        return jsonify({'message': f'Key "{key}" not found'}, 404)
    else:
        return jsonify({'message': f'Value for key {key} updated successfully'}, 200)

@app.route('/read/<key>', methods=['GET'])
def read_value(key):
    item = mongo.db.items.find_one_or_404({'key': key})
    return parse_json(item), 200

if __name__ == "__main__":
    app.run(debug=True)
