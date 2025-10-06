import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('Word_API')

word = 'apple'
url = f"https://www.dictionaryapi.com/api/v3/references/learners/json/{word}?key={api_key}"

response = requests.get(url)
data = response.json()

for i in range(len(data)):
    print(data[i]['meta']['app-shortdef']['hw'])
    print(data[i]['meta']['app-shortdef']['fl'])
    print(data[i]['meta']['app-shortdef']['def'][0])
    print()