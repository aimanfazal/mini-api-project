import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NEWS_API_KEY")

if not api_key:
raise ValueError("NEWS_API_KEY not found in .env file")

url = (
f"https://newsapi.org/v2/top-headlines?"
f"country=us&category=business&apiKey={api_key}"
)

try:
response = requests.get(url, timeout=10)
response.raise_for_status()

```
news = response.json()

for article in news["articles"]:
    print(f"📰 {article['title']}")
    print(article["description"])
    print("-" * 80)
```

except requests.exceptions.RequestException as e:
print(f"Error fetching news: {e}")
