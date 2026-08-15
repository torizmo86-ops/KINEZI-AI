import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

with open("brain.md", "r", encoding="utf-8") as file:
    brain = file.read()

print("KINEZI AI прочете своя мозък:")
print(brain)
