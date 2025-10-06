# 🧩 Mini API Project

This repository contains two simple Python programs that helped me understand how APIs work and how to use them in Python.

## 🚀 Overview

1. **Random Quote Generator** — Fetches a random quote from different categories using the [DailyQuotes API](https://dailyquotes.dev/).
2. **Dictionary Lookup Tool** — Fetches word definitions using the [Merriam-Webster Dictionary API](https://dictionaryapi.com/).

These programs demonstrate:
- How to use `requests` to interact with REST APIs  
- How to handle JSON data  
- How to securely load API keys using environment variables (`.env` file)

---

## 🔑 Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/mini-api-project.git
    cd mini-api-project

2. Install dependencies:
    ```bash
    pip install requests python-dotenv

3. Create a .env file in your project directory and add your API keys:
    ```ini
    API_KEY=your_dailyquotes_api_key
    Word_API=your_dictionary_api_key

4. Run the programs:
    ```bash
    python quotes_api.py
    python dictionary_api.py