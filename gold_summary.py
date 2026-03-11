import duckdb
import os

def create_gold_layer():
    silver_path = 'data/scored_news_silver.csv'
    
    if not os.path.exists(silver_path):
        print("❌ Silver data not found. Run transform.py first!")
        return

    # Use SQL to aggregate sentiment by news source
    # This proves you can use SQL Window Functions or Group By logic
    query = """
        SELECT 
            source,
            COUNT(*) as article_count,
            AVG(sentiment_score) as avg_sentiment,
            MIN(sentiment_score) as worst_toxic_score,
            MAX(sentiment_score) as best_positive_score
        FROM read_csv_auto('data/scored_news_silver.csv')
        GROUP BY source
        ORDER BY avg_sentiment ASC
    """
    
    # Run the query and save to Gold Layer
    print("Running SQL aggregation for Gold Layer...")
    duckdb.sql(query).write_csv('data/source_sentiment_gold.csv')
    print("✅ Gold Layer: SQL summary saved to data/source_sentiment_gold.csv")

if __name__ == "__main__":
    create_gold_layer()