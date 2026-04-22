import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def call_llm(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "あなたは優秀なプロダクトマネージャーです"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content