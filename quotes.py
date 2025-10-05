import requests
import os
from dotenv import load_dotenv


url = "https://api.dailyquotes.dev/api/quotes/motivational"
headers = {
    "Authorization": "Bearer API_Key",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)