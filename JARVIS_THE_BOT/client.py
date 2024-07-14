# use of openai to get responses form the chatgpt 

from openai import OpenAI
client = OpenAI(
    api_key="sk-proj-7OoBvhfnUa8eWzABSPsDT3BlbkFJxBsM46VebfTmVYMwokJb",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)