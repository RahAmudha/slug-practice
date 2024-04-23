from flask import Flask, request, jsonify,Blueprint
from app.controllers.api_controller import process_request_simple


app = Flask(__name__)

@app.route('/api/openai/simple', methods=['POST'])
def openai_route_simple():
    data = request.json
    return process_request_simple(data)

@app.route('/api/openai/mc', methods=['POST'])
def openai_route_mc():
    data = request.json
    return send_to_openai(data)

@app.route('/api/openai/tf', methods=['POST'])
def openai_route_tf():
    data = request.json
    return send_to_openai(data)

if __name__ == '__main__':
    app.run()