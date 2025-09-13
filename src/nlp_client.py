# This file will handle the natural language processing to create the reason and result columns in the database

from openai import OpenAI
import json

# set API key in environment variables once created
client = OpenAI(api_key="hardcode-or-use-env-var")

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