# AI-News-Analysis

AI News Analysis application allows users to view news articles categorized by region, sentiment (positive, negative, neutral), and topic. Users can register, log in, and access content based on these categories.

## Key Features:
- **User Authentication**: Users can register, log in, and log out.
- **Region & Sentiment Views**: Articles are displayed by region and sentiment.
- **News Aggregation**: Articles are scraped from Google News (via the `GoogleNews` Python library), analyzed for sentiment using FinBERT, and stored in the database.

## Backend:
- Sentiment analysis is performed with **FinBERT**.
- News is categorized and saved based on sentiment.
- The system supports dynamic content fetching and categorization.

## Technologies:
- **Django** for the backend.
- **FinBERT** for sentiment analysis.
- **GoogleNews Python library** for fetching articles.
