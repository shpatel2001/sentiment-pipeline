import requests
import json
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Get API Key from environment variable
API_KEY = os.getenv('NEWS_API_KEY')
TOPIC = 'technology'

def fetch_bronze_data():
    if not API_KEY:
        print("❌ Error: NEWS_API_KEY not found. Check your .env file!")
        return

    print(f"Fetching news about {TOPIC}...")
    url = f'https://newsapi.org/v2/everything?q={TOPIC}&apiKey={API_KEY}&language=en'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Save to the data folder
            with open('data/raw_news.json', 'w') as f:
                json.dump(data, f, indent=4)
            print("✅ Bronze Layer: Raw data saved to data/raw_news.json")
        else:
            print(f"❌ Failed to fetch data: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
    fetch_bronze_data()