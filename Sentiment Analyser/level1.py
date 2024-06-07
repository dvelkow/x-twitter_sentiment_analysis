
# level 1, breaks sentances up and sends them to be analysed to lvl 0
from level0 import calculate_sentiment

def analyze_sentiment(text):
    # Split text based on periods and commas
    chunks = [chunk.strip().lower() for chunk in text.replace('.', ',').split(',') if chunk.strip()]

    overall_sentiment_score = 0
    chunk_count = len(chunks)

    for chunk in chunks:
        sentiment_score = calculate_sentiment(chunk)
        overall_sentiment_score += sentiment_score

    # Calculate the final overall sentiment score
    if chunk_count > 0:
        average_sentiment_score = overall_sentiment_score / chunk_count
    else:
        average_sentiment_score = 0.5  # Neutral if no chunks found

    # Determine sentiment based on average sentiment score
    if average_sentiment_score > 0.55:
        final_sentiment = 1  # Positive
    elif average_sentiment_score < 0.45:
        final_sentiment = -1  # Negative
    else:
        final_sentiment = 0  # Neutral

    return final_sentiment