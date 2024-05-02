"""
Service the api request i.e parse...
"""
from flask import jsonify
from openai import OpenAI
import os


def make_openai_request(prompt):

    APIKEY = os.environ.get("OPENAI_SLUG_PRACTICE_API_KEY")    
    client = OpenAI(api_key= APIKEY)
    
    print(prompt)
    
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        response_format =  {"type": "json_object"},
        
        messages = [
                {"role": "system", "content": "You are a machine that creates practice problems and answers for students. "}, # Tweak this?
                {"role": "user", "content": prompt }
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
You are a bot that generates practice problems based on an academic keyword, difficulty, and the example that the user gives.
The difficulty can be a number between 1 and 10, with 1 being the easiest and 10 being the hardest.
Generate 10 problems and answers about %s at difficulty level %s and based on this example: %s. In JSON format.
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
You are a bot that generates practice problems based on an academic keyword, difficulty, and the example that the user gives.
The difficulty can be a number between 1 and 10, with 1 being the easiest and 10 being the hardest.
Generate 10  true and false problems with answers about %s at difficulty level %s and based on this example: %s. In JSON format.
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
You are a bot that generates practice problems based on an academic keyword, difficulty, and the example that the user gives.
The difficulty can be a number between 1 and 10, with 1 being the easiest and 10 being the hardest.
Generate 10  multiple choice questions and answers with answers about %s at difficulty level %s and based on this example: %s. In JSON format.
    """
    generated_prompt = prompt % (topic, difficulty, example)
    response = make_openai_request(generated_prompt)
    return response
