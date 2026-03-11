# Voice Intelligence & Media Sentiment Pipeline

An end-to-end data engineering pipeline designed to audit online media for "toxicity" and sentiment. Built to demonstrate automated ETL, secrets management, and containerization.

## Architecture (Medallion Model)
- **Bronze:** Python-based ingestion of raw news data via API.
- **Silver:** NLP processing using `TextBlob` to generate sentiment scores.
- **Gold:** Analytical aggregation via `DuckDB` (SQL) to identify high-risk sources.

## Tech Stack
- **Language:** Python 3.11
- **Orchestration:** Docker (Containerized workflow)
- **Database:** DuckDB (In-memory SQL)
- **Visualization:** [View Live Tableau Dashboard](https://public.tableau.com/app/profile/shayen.patel/viz/VoiceIntelligenceMediaSentimentMonitor/MediaSentimentPipelineMedallionArchitectureInsights?publish=yes)

## How to Run
1. Clone the repo.
2. Create a `.env` file with your `NEWS_API_KEY`.
3. Run `docker build -t sentiment-pipeline .`
4. Run `docker run --env-file .env -v "${PWD}/data:/app/data" sentiment-pipeline`
