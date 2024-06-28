import os
import sys
from typing import List
import tweepy
from level1 import analyze_sentiment

# Add the current directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from config import (
    TWITTER_CREDENTIALS,
    SENTIMENT_RANGES,
    SENTIMENT_MESSAGES,
    DEFAULT_QUERY,
    DEFAULT_TWEET_COUNT
)

def setup_twitter_client():
    client = tweepy.Client(
        consumer_key=TWITTER_CREDENTIALS['consumer_key'],
        consumer_secret=TWITTER_CREDENTIALS['consumer_secret'],
        access_token=TWITTER_CREDENTIALS['access_token'],
        access_token_secret=TWITTER_CREDENTIALS['access_token_secret']
    )
    return client

def fetch_tweets(query: str, count: int = DEFAULT_TWEET_COUNT) -> List[str]:
    client = setup_twitter_client()
    tweets = tweepy.Paginator(
        client.search_recent_tweets,
        query=query,
        tweet_fields=['context_annotations', 'created_at'],
        max_results=10
    ).flatten(limit=count)
    return [tweet.text for tweet in tweets]

def calculate_overall_score(total_score: float, analyzed_tweets: int) -> float:
    return ((total_score / analyzed_tweets) + 1) * 50 if analyzed_tweets > 0 else 50

def get_sentiment_message(score: float) -> str:
    for low, high, sentiment in SENTIMENT_RANGES:
        if low <= score < high:
            return SENTIMENT_MESSAGES[sentiment]
    return SENTIMENT_MESSAGES['neutral']  # Default case

def analyze_tweets(query: str, count: int = DEFAULT_TWEET_COUNT) -> None:
    tweets = fetch_tweets(query, count)
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
    analyze_tweets(DEFAULT_QUERY, DEFAULT_TWEET_COUNT)
