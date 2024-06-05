"""
Service the api request i.e parse...
"""
from flask import jsonify
from openai import OpenAI
import os


def make_openai_request(user_prompt):

    APIKEY = os.environ.get("OPENAI_SLUG_PRACTICE_API_KEY")    
    client = OpenAI(api_key= APIKEY)
    
    print(user_prompt)
    
    system_prompt = """You are a bot that generates practice questions and answers based on an academic keyword, difficulty, and the example that the user gives.
    The difficulty can be easy, medium, or hard, with 'easy' being easy, 'med' being medium, and 'hard' being hard. Respond in a JSON format so that the overall structure is a 
    dictionary that contains a key "questions" whose value is an array.
    The array, in turn, contains a dictionary with keys "question" and "answer" and their respective string values."""
    
    response = client.chat.completions.create(
        model = "gpt-4o",
        response_format =  {"type": "json_object"},
        
        messages = [
                {"role": "system", "content":system_prompt}, 
                {"role": "user", "content": user_prompt }
                ],

            
            temperature=0.7 ## need a function here to determine diffifcultity
            #temperature = get_temp(difficulty) spits out a number between 0 and 2
         )

    return response.choices[0].message.content


# Service the Simple Request
def service_simple(data):
    topic = data['topic']
    example = data['example']
    difficulty = data['difficulty']
    
    #! prompt engineered goes here
    prompt = """
Generate 10 problems and answers about %s at difficulty level %s and based on this example: %s. With questions being the name of the array and 'question'
and 'answers' being the keys
    """
    generated_prompt = prompt % (topic, difficulty, example)

    
    response = make_openai_request(generated_prompt)
    return response

# Service the True/False Request
def service_tf(data):
    topic = data['topic']
    example = data['example']
    difficulty = data['difficulty']
    
    #! prompt engineered goes here
    prompt = """
Generate 10 true and false problems with answers about %s at difficulty level %s and based on this example: %s. Indicate that this is a True or False question
by writing 'TRUE or FALSE: ' at the beginning of the question.
    """
    generated_prompt = prompt % (topic, difficulty, example)
    response = make_openai_request(generated_prompt)
    return response
    



# Service the MC request
def service_mc(data):
    topic = data['topic']
    example = data['example']
    difficulty = data['difficulty']
    
    #! prompt engineered goes here
    prompt = """
Generate 10 Multiple Choice questions and answers with options about %s at difficulty level %s and based on this example: %s. 
With 'questions' being the name of the array, 
'question' being a key for every question,
'choice' being a key value pair where the value is an array with the choices labeled 'A', 'B', or 'C',
and 'answers' being the key for right option
    """
    generated_prompt = prompt % (topic, difficulty, example)
    response = make_openai_request(generated_prompt)
    return response
