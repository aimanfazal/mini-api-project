import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')
url = "https://api.dailyquotes.dev/api/quotes/motivational"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)