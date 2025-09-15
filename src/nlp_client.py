# This file will handle the natural language processing to create the reason and result columns in the database

from openai import OpenAI
import json
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

with open("query_params.json", "r") as f:
    QUERY_CONFIGS = json.load(f)

def query_openai(config_name: str, transcript: str) -> str:

    if config_name not in QUERY_CONFIGS:
        raise ValueError(f"Unknown config '{config_name}'")

    params = QUERY_CONFIGS[config_name]

    response = client.chat.completions.create(
        n=params.get("number"),
        model=params.get("model"),
        temperature=params.get("temperature"),
        top_p=params.get("top_p"),
        response_format=params.get("response_format", "text"),
        messages=[
            {"role": "system", "content": params.get("system")},
            {"role": "user", "content": transcript},
        ],
    )

    return response.choices[0].message.content