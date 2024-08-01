import os

os.environ["OPENAI_API_KEY"] = "XXX"
os.environ["GROQ_API_KEY"] = "YYY"

from routellm.controller import Controller

client = Controller(
  routers=["mf"],
  strong_model="gpt-4-1106-preview",
  weak_model="groq/llama3-8b-8192"
)

response = client.chat.completions.create(
  # This tells RouteLLM to use the MF router with a cost threshold of 0.11593
  model="router-mf-0.11593",
  messages=[
    {"role": "user", "content": "Write the game snake in python"}
  ]
)

message_content = response['choices'][0]['message']['content']
model_name = response['model']

print(f"Message content: {message_content}")
print(f"Model name: {model_name}")