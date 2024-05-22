from openai import OpenAI
import os




def isValid(user_data):

    APIKEY = os.environ.get("OPENAI_SLUG_PRACTICE_API_KEY")

    client = OpenAI(api_key= APIKEY)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system", 
                "content": """You are a validation program. You will receive two inputs: a topic and an example question. Validate the inputs as follows:
                1. If the topic is not a valid academic topic, reply with '1'.
                2. If the example question is not appropriate or related to the topic, reply with '2'.
                3. If the examples are not related reply with '3'
                4. If both inputs are valid and related, reply with '4'."""
            },
            {
                "role": "user", 
                "content": f"User Topic: {user_data['topic']} User Example: {user_data['example']}"
            }
        ]
    )

   
    return response.choices[0].message.content


