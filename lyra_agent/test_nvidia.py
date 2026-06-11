import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

print("KEY FOUND:", bool(os.getenv("NVIDIA_API_KEY")))
print("KEY PREFIX:", os.getenv("NVIDIA_API_KEY", "")[:10])

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

response = client.chat.completions.create(
    model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning",

    messages=[
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=10,
    temperature=0,
)

print(response)