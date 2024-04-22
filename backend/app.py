from flask import Flask, request, jsonify,Blueprint
from app.controllers.api_controller import send_to_openai

app = Flask(__name__)

@app.route('/api/openai', methods=['POST'])
def openai_route():
    return send_to_openai(request)

if __name__ == '__main__':
    app.run()