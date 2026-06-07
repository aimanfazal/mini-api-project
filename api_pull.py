import requests
import json

# query = input("What updates do you want to get? ")
url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=a35555a8178043c1844fbb10fbe13615"

r = requests.get(url)

news = json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print()