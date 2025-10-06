import requests
import os
from dotenv import load_dotenv

load_dotenv()

categories = ['quotes', 'anime', 'movie', 'dev', 'motivational', 'self_improvement', 'game', 'book', 'poetry', 'mentalhealth']
print("Welcome to Random Quote Generator Program!")

for cat in range(len(categories)):
    print(f"{cat + 1} = {categories[cat]}")

i = int(input("Select the category of the quote211qqew: ")) - 1

api_key = os.getenv('API_KEY')

url = f"https://api.dailyquotes.dev/api/quotes/{categories[i]}"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)