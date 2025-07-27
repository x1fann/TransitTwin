from flask import Blueprint, request, jsonify
from database import fetch_data
import subprocess

routes = Blueprint('routes', __name__)

@routes.route('/get-data-by-moment', methods=['GET'])
def get_moment_data():
    moment = request.args.get('moment')
    query = "SELECT * FROM track_data_1 WHERE moment = %s"
    result = fetch_data(query, (moment,))
    return jsonify(result)

@routes.route('/get-data-by-name', methods=['GET'])
def get_data_by_name():
    name = request.args.get('name')
    query = "SELECT * FROM track_data_1 WHERE name = %s"
    result = fetch_data(query, (name,))
    return jsonify(result)

def execute_script(script_path):
    try:
        process = subprocess.Popen(
            ['python', script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            errors='replace'
        )
        output, error = process.communicate()

        if error:
            return {'error': error}, 500

        return {'result': output}
    except Exception as e:
        return {'error': str(e)}, 500

@routes.route('/predict', methods=['GET'])
def predict():
    return jsonify(execute_script('Backend/扣件失效判识算法/test_3.py'))

@routes.route('/predict1', methods=['GET'])
def predict1():
    return jsonify(execute_script('Backend/预测算法/test_1.py'))

@routes.route('/predict2', methods=['GET'])
def predict2():
    return jsonify(execute_script('Backend/预测算法/test_2.py'))
