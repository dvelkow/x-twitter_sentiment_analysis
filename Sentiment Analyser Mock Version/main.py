import os
import sys
from typing import List

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from level1 import analyze_sentiment
from config import EXAMPLE_TWEETS, SENTIMENT_RANGES, SENTIMENT_MESSAGES

def calculate_overall_score(total_score: float, analyzed_tweets: int) -> float:
    return ((total_score / analyzed_tweets) + 1) * 50 if analyzed_tweets > 0 else 50

def get_sentiment_message(score: float) -> str:
    for low, high, sentiment in SENTIMENT_RANGES:
        if low <= score < high:
            return SENTIMENT_MESSAGES[sentiment]
    return SENTIMENT_MESSAGES['neutral']  # Default case

def analyze_tweets(tweets: List[str]) -> None:
    total_score = 0
    analyzed_tweets = 0

    for i, tweet in enumerate(tweets, 1):
        sentiment = analyze_sentiment(tweet)
        total_score += sentiment
        analyzed_tweets += 1
        print(f"Tweet {i}: {tweet}")
        print(f"Sentiment: {sentiment}\n")

    overall_score = calculate_overall_score(total_score, analyzed_tweets)
    message = get_sentiment_message(overall_score)

    print(f"Overall Sentiment Score: {overall_score:.2f}")
    print(message)

if __name__ == "__main__":
    analyze_tweets(EXAMPLE_TWEETS)