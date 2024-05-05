from flask import Flask, request, jsonify,Blueprint, render_template
from app.controllers.api_controller import*
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# enable CORS for all routes and origins
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/api/openai/simple', methods=['POST'])
def openai_route_simple():
    """
    Endpoint for processing simple OpenAI requests.

    This endpoint accepts a POST request with a JSON payload containing the necessary data
    for processing a simple OpenAI request. The request is forwarded to the `process_request_simple`
    function in the `api_controller` module for further processing.

    Returns:
    if pass:
        Status => Success && Simple questions and answers based on users topic and difficulty in JSON format
    otherwise:
        Status =>Fail && no data

Example:        
        {
"questions": [
{
"question": "Who was the first President of the United States?",
"answer": "George Washington"
},
{
"question": "What was the outcome of the Civil War?",
"answer": "Union victory and abolition of slavery"
},
{
"question": "Which event led to the United States entering World War II?",
"answer": "The attack on Pearl Harbor by Japan"
},
    """
    data = request.json
    return process_request_simple(data)

@app.route('/api/openai/tf', methods=['POST'])
def openai_route_tf():
    """
    Endpoint for processing OpenAI requests with true/false questions.

    This endpoint accepts a POST request with a JSON payload containing the necessary data
    for processing an OpenAI request with true/false questions. The request is forwarded to the
    `proces_requrest_tf` function in the `api_controller` module for further processing.

    Returns:
        if pass:
            Status = Success && True and False Question with Anwsers 
        otherwise:
            Status = Fail && No data
            
            Example Response
            
    "questions": [
        {
            "question": "Is it true that 2 + 2 = 5?",
            "answer": false
        },
        {
            "question": "Is it true that 7 x 3 = 21?",
            "answer": true
        },
        {
            "question": "Is it true that the square root of 16 is 5?",
            "answer": false
        }
        ]
    
    """
    data = request.json
    return process_request_tf(data)

@app.route('/api/openai/mc', methods=['POST'])
def openai_route_mc():
    """
    Endpoint for processing OpenAI requests with multiple choice.

    This endpoint accepts a POST request with a JSON payload containing the necessary data
    for processing an OpenAI request with multiple choice. The request is forwarded to the
    `process_request_mc` function in the `api_controller` module for further processing.

    Returns:
        if pass:
            Status = Success && Multiple Choice questions with marked anwsers 
        otherwise:
            Status = Fail && No data
            
    Example Response:
    
{
    "questions": [
        {
            "question": "What is voltage?",
            "options": {
                "a": "The flow of electric charge",
                "b": "The measure of electric potential difference between two points",
                "c": "The unit of current",
                "d": "The resistance to electric current flow"
            },
            "correct_answer": "b"
        }
                ]
}

    """
    data = request.json
    return process_request_mc(data)

@app.route('/') 
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()