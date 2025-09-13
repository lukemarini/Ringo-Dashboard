# This file is a placeholder for making requests to the retell API

import requests

def fetch_calls():
    """
    Placeholder function.
    Later: make requests to Retell API.
    """
    return [
        {
            "phone_number": "+15551234567",
            "direction": "incoming",
            "start_time": "2025-09-13 14:00:00",
            "end_time": "2025-09-13 14:15:00",
            "duration_seconds": 900,
            "reason": "Buying inquiry",
            "result": "Home showing booked",
            "transcript": "CALLER: Hi\nAI: Hello, why are you calling?\nCALLER: I want to buy a house\nAI: Okay, here are some properties…"
        }
    ]


'''
API_KEY = "your-retell-api-key"
BASE_URL = "https://api.retell.ai/v1/calls"

def fetch_calls():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(BASE_URL, headers=headers)
    response.raise_for_status()
    data = response.json()

    # Transform Retell’s response into our schema format
    calls = []
    for call in data["calls"]:
        calls.append({
            "phone_number": call["caller"]["phoneNumber"],
            "direction": call["direction"],
            "start_time": call["startTime"],
            "end_time": call["endTime"],
            "duration_seconds": call["duration"],
            "reason": None,  # placeholder, NLP or manual input later
            "result": None,  # placeholder
            "transcript": call["transcript"]
        })
    return calls
'''