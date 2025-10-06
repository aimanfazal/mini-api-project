import requests
import os
from dotenv import load_dotenv

def load_API():
    '''Loads API Key from the environment variables (".env file")'''

    load_dotenv()
    return os.getenv('API_KEY')

def displayCatogories(categories):
    '''Displays the list of available quote categories'''

    print("Welcome to the \"Random Quote Generator\" program!\n")
    print("Available categories: ")
    for idx, category in enumerate(categories, start=1):
        print(f"{idx}. {category}")

def userChoice(categories):
    '''prompts the user to select a valid category'''

    choice = int(input("\nSelect the category: "))
    try:
        if 1 <= choice <= len(categories):
            return categories[choice - 1]
        else:
            print("Invalid selection! Please select a valid number (1-10)")
            return userChoice(categories)  
    except ValueError:
        print("Invalid input! Enter only integer numbers (1-10)")
        return userChoice(categories)

def fetchQuote(category, api_key):
    '''fetches API from the endpoint, also checks the status code'''

    url = f"https://api.dailyquotes.dev/api/quotes/{category}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch quote. Status code: {response.status_code}"}

def main():
    '''function with the core tasks'''
    
    categories = ['quotes', 'anime', 'movie', 'dev',
                  'motivational','self_improvement',
                  'game', 'book', 'poetry', 'mentalhealth']
    
    api_key = load_API()
    if not api_key:
        print("No API key found! Please check your .env file.")
        return
    
    displayCatogories(categories)
    choice = userChoice(categories)
    quoteData = fetchQuote(choice, api_key)

    print()
    for key, value in quoteData.items():
        print(f"{key.title()}: {value}")

if __name__ == "__main__":
    main()