import requests
import os

api_key = "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"
url = "https://api.groq.com/openai/v1/models"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print(response.json())