import os
import requests
from openai import OpenAI
from flask import jsonify

from dotenv import load_dotenv

load_dotenv()


def send_to_openai(request):
    try:
        APIKEY = os.environ.get("OPENAI_SLUG_PRACTICE_API_KEY")
        url = 'https://api.openai.com/v1/chat/completions'
        headers = {
            'Authorization': f'Bearer {APIKEY}',
            'Content-Type': 'application/json',
        }
        print(APIKEY)
        response = requests.post(url, json=request.json, headers=headers)
        response.raise_for_status()

        response_json = response.json()

        
        message = response_json['choices'][0]['message']['content']
        print('Message',message)
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

# def sent_to_openai(request):
#     try:
#         APIKEY = os.environ.get("OPENAI_SLUG_PRACTICE_API_KEY")
#         client = OpenAI(
#         api_key= APIKEY
#         )

#         response = client.chat.completions.create(
#             model = "gpt-3.5-turbo",
#             response_format={"type": "json_object"},
#             messages = [
#                 {"role": "system", "content": "You are Jack Sparrow"},
#                 {"role": "user", "content": "Hello mr pirate" }
       
#                 ],
#             stream=True
#         )
# # stream can only be iterated once btw
#         res = []
#         for chunk in response:
#             if chunk.choices[0].delta.content is not None:
#                 res.append(chunk.choices[0].delta.content)
#         print("".join(res))

#         return res
    
#     except requests.exceptions.RequestException as e:
#         return jsonify({'error': str(e)}), 500

