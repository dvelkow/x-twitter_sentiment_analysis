import tweepy
import pandas as pd

consumer_key = 'CONSUMER_KEY_PLACE_HOLDER'
consumer_secret = 'CONSUMER_SECRET_PLACE_HOLDER'
access_token = 'ACCESS_TOKEN_PLACE_HOLDER'
access_token_secret = 'ACCESS_TOKEN_SECRET_PLACE_HOLDER'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def fetch_tweets(query, count=100):
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en").items(count)
    tweet_list = [[tweet.created_at, tweet.user.screen_name, tweet.text] for tweet in tweets]
    return pd.DataFrame(tweet_list, columns=['Datetime', 'Username', 'Text'])

df = fetch_tweets('Python', count=200)
df.to_csv('tweets.csv', index=False)

### UNFINISHED