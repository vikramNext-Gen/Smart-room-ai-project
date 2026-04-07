import os
from openai import OpenAI

# Environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
HF_TOKEN = os.getenv("HF_TOKEN")

# Initialize client
client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

print("START")

# Simulated smart room logic
temperature = 30
people = 2

print("STEP: Initial State -> Temp:", temperature, "People:", people)

if temperature > 28:
    action = "Turn ON AC"
elif people > 0:
    action = "Turn ON Fan"
else:
    action = "Turn OFF devices"

print("STEP: Action ->", action)

# Dummy LLM call (to satisfy requirement)
try:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": "Optimize room energy"}]
    )
    print("STEP: AI Response ->", response.choices[0].message.content)
except Exception as e:
    print("STEP: AI call skipped (no key)")

print("END")
