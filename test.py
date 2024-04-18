from openai import OpenAI

client = OpenAI(
    api_key="richard jullig"
)

stream = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [{"role": "user", "content": "say gex" }],
    stream=True
)
# stream can only be iterated once btw
res = []
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        res.append(chunk.choices[0].delta.content)
print("".join(res))