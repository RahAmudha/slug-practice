"""
Service the api request i.e parse...
"""
from openai import OpenAI
import os

#Does the same thing but less flexible up to yall

def sent_to_openai(data):
    topic = data['topic']
    example = data['example']
    difficulty = data['difficulty']
    
    prompt = "Give me 5 questions and answers for this topic: %s. Like this: %s " % (topic,example)
    APIKEY = os.environ.get("OPENAI_SLUG_PRACTICE_API_KEY")
    
    client = OpenAI(
    api_key= APIKEY
    )

    print(prompt)

    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
                {"role": "system", "content": "You are tutor"},
                {"role": "user", "content": prompt }
                ],
            stream=True,
            temperature=0.7 ## need a function here to determine diffifcultity
            #temperature = get_temp(difficulty) spits out a number between 0 and 2
         )
# # stream can only be iterated once btw
    res = []
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            res.append(chunk.choices[0].delta.content)
    print("".join(res))

    ## Parse questions and answers
    ## res = parse() we want json with questions and answers

    return res

"""
tested via postman
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

"""