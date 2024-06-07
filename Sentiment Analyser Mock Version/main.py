# level 2/ main, collects tweets and sends them to lvl 1 to be analysed
from level1 import analyze_sentiment

example_tweets = [
    "Bitcoin is looking good on the 4H, feeling bullish $BTC",
    "The crash of $BTC is causing a lot of fear and panic selling.",
    "My model is predicting a significant increase in $BTC in the short term.",
    "This dip is not looking good, more blood to come $BTC",
    "The new regulations might impact Bitcoin prices negatively. $BTC",
    "I am very bullish on Bitcoin right now, thinking about longing $BTC",
    "The FOMO is soon going to manifest itself and drive more people to buy $ETH",
    "A big on-chain hack is happening right now, will likely affect the price, so bearish short term $BTC $ETH",
    "Bitcoin's showing some signs of life, looking solid so far. $BTC",
    "People are still cautious despite the uptrend in $BTC, which means more future buy pressure $BTC"
]

def analyze_tweets(tweets):
    total_score = 0
    analyzed_tweets = 0

    for tweet in tweets:
        sentiment = analyze_sentiment(tweet)
        total_score += sentiment
        analyzed_tweets += 1
        print(f"Tweet {analyzed_tweets}: {tweet}")
        print(f"Sentiment: {sentiment}\n")

    # Calculating the overall sentiment score (0-100), 50 would be neutral here
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
    print(f"{message}")

# Run the analysis on example tweets
analyze_tweets(example_tweets)