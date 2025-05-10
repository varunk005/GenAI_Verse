import os
import requests
from dotenv import load_dotenv

# Load token
load_dotenv()
API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Set model and API URL
API_URL = "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Query function
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    try:
        return response.json()
    except Exception:
        return {"error": "Failed to parse JSON response", "text": response.text, "status": response.status_code}

# Prepare input
data = {
    "inputs": "User: What is artificial intelligence?\nAssistant:",
    "parameters": {
        "max_new_tokens": 200,
        "temperature": 0.7
    }
}

# Make request
response = query(data)

# Show output
print(response)
