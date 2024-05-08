from flask import Flask, request, jsonify,Blueprint, render_template
from app.controllers.api_controller import*
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# enable CORS for all routes and origins
CORS(app, resources={r"/*": {"origins": "*"}})

# Applied DRY Principle
@app.route('/openai/generate',methods=['POST'])
def generate():
    data = request.json
    return process_request(data)
    
    

@app.route('/') 
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()