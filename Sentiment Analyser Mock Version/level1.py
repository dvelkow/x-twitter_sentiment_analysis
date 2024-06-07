# level 1, breaks sentances up and sends them to be analysed to lvl 0
from level0 import calculate_sentiment

def analyze_sentiment(text):
    # Split text based on periods and commas
    chunks = [chunk.strip() for chunk in text.replace('.', ',').split(',') if chunk.strip()]

    overall_sentiment_score = 0
    chunk_count = len(chunks)

    for chunk in chunks:
        sentiment_score = calculate_sentiment(chunk)
        if sentiment_score > 0:
            sentiment = 1  # Positive sentiment
        elif sentiment_score < 0:
            sentiment = -1  # Negative sentiment
        else:
            sentiment = 0  # Neutral sentiment
        
        overall_sentiment_score += sentiment_score

    # Calculate the final overall sentiment score (1, 0, or -1)
    if overall_sentiment_score > 0:
        final_sentiment = 1
    elif overall_sentiment_score < 0:
        final_sentiment = -1
    else:
        final_sentiment = 0

    return final_sentiment