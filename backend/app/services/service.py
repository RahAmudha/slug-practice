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
                {"role": "system", "content": "You are tutor"}, # Tweak this?
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
    
    #! prompt engineered goes here
    prompt = "Give me 5 questions and answers for this topic: %s. Like this: %s in json format" % (topic, example)
    
    response = make_openai_request(prompt)
    return response

# Service the True/False Request
def service_tf(data):
    topic = data['topic']
    example = data['example']
    
    #! prompt engineered goes here
    prompt = "Give me 5 True False for this topic: %s. Like this: %s in json format" % (topic, example)
    
    response = make_openai_request(prompt)
    return response
    



# Service the MC request
def service_mc(data):
    topic = data['topic']
    example = data['example']
    
    #! prompt engineered goes here
    prompt = "Give me 5 Multiple Choice for this topic: %s. Like this: %s in json format" % (topic, example)
    
    response = make_openai_request(prompt)
    return response
