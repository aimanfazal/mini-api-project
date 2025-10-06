import requests
import os
from dotenv import load_dotenv

def fetch_definitions(word):
    load_dotenv()
    api_key = os.getenv('Word_API')

    if not api_key:
        print("API Key not found! Check the .env file.")
        return

    url = f"https://www.dictionaryapi.com/api/v3/references/learners/json/{word}?key={api_key}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data! Status Code: {response.status_code}")
        return

    data = response.json()

    print(f"\n-- Definitons for {word} --\n")

    for entry in data:
        try:
            shortdef = entry['meta']['app-shortdef']
            headword = shortdef['hw']
            part_of_speech = shortdef['fl']
            definition = shortdef['def'][0]

            print(f"Word: {headword}")
            print(f"Part of Speech: {part_of_speech}")
            print(f"Definition: {definition}\n")

        except KeyError:
            continue

if __name__ == "__main__":
    word = input("Looking for the perfect word? ").strip()
    fetch_definitions(word)