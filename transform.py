import json
import pandas as pd
import os
from textblob import TextBlob

def create_silver_layer():
    raw_path = 'data/raw_news.json'
    
    if not os.path.exists(raw_path):
        print("❌ Bronze data not found. Run ingest.py first!")
        return

    with open(raw_path, 'r') as f:
        data = json.load(f)

    articles = data.get('articles', [])
    processed_data = []

    for a in articles:
        # Use TextBlob to analyze the headline sentiment
        # Polarity: -1.0 (Very Negative/Toxic) to 1.0 (Very Positive)
        text = a.get('title', '')
        score = TextBlob(text).sentiment.polarity
        
        processed_data.append({
            'source': a['source']['name'],
            'author': a.get('author'),
            'title': text,
            'sentiment_score': score,
            'published_at': a['publishedAt']
        })

    # Save as Silver Layer (Structured CSV)
    df = pd.DataFrame(processed_data)
    df.to_csv('data/scored_news_silver.csv', index=False)
    print(f"✅ Silver Layer: Processed {len(df)} articles into data/scored_news_silver.csv")

if __name__ == "__main__":
    create_silver_layer()