from openai import OpenAI
import os

#print(os.environ)
APIKEY = os.environ.get("OPENAI_SLUG_PRACTICE_API_KEY")

client = OpenAI(
    api_key= APIKEY
)

stream = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
         {"role": "system", "content": "You are Jack Sparrow"},
        {"role": "user", "content": " Hello, what does your compass do?" }
       
        ],
    stream=True
)
# stream can only be iterated once btw
res = []
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        res.append(chunk.choices[0].delta.content)
print("".join(res))