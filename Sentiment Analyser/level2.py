# level2, collects tweets and sends them to lvl 1 to be analysed

import tweepy
from level1 import analyze_sentiment

#access_token = '1789438181906993152-tUTFq17OOzNKmM9kaUk72Ske4tNrea'
#access_token_secret = 'QCPwdFRyl0P6lzkYwFgZNBPocvdNVwUPmnstUhnEHbWdt'
#bearer_token = 'AAAAAAAAAAAAAAAAAAAAAJKyuAEAAAAAduVxRaPAutE0ojivSVGPbNNiUcw%3DpLQ5KPVxKDV1Q6qISCx7mpc9ORsmaF7OwRuZaiI04dHxQVA8zM'

# Authenticate to Twitter using the Bearer token
#client = tweepy.Client(bearer_token=bearer_token)

def fetch_tweets(query, count=100):
    tweets = tweepy.Paginator(client.search_recent_tweets, query=query, tweet_fields=['context_annotations', 'created_at'], max_results=10).flatten(limit=count)
    tweet_list = [tweet.text for tweet in tweets]
    return tweet_list

def analyze_tweets(query, count=100):
    tweets = fetch_tweets(query, count)
    total_score = 0
    analyzed_tweets = 0

    for tweet in tweets:
        sentiment = analyze_sentiment(tweet)
        total_score += sentiment
        analyzed_tweets += 1
        print(f"Tweet: {tweet}")
        print(f"Sentiment: {sentiment}\n")

    # Calculating the overall sentiment score (0-100), 50 would be netural here
    if analyzed_tweets > 0:
        overall_score = ((total_score / analyzed_tweets) + 1) * 50
    else:
        overall_score = 50

    # Displaying an appropriate message based on the overall sentiment score
    if overall_score < 20:
        message = "The sentiment is overly negative. Twitter users are most likely in shorts. (spot sell pressure, futures short pressure)"
    elif overall_score < 45:
        message = "The sentiment is somewhat negative. Twitter users are most likely just selling, and a few might be shorting. (spot neutral, futures short pressure)"
    elif overall_score <= 55:
        message = "The sentiment is mixed. No alpha can be gained from the feed."
    elif overall_score <= 80:
        message = "The sentiment is positive. Twitter users are most likely just holding, and a few might be longing.(spot neutral, futures long pressure)"
    else:
        message = "The sentiment is overly positive. Twitter users are most likely in longs.(spot buy pressure, futures long pressure)"

    print(f"Overall Sentiment Score: {overall_score:.2f}")
    print(f"Message: {message}")

if __name__ == "__main__":
    query = "$BTC"  # Example query
    analyze_tweets(query, count=100)
