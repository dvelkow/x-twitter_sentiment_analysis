EXAMPLE_TWEETS = [
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

SENTIMENT_RANGES = [
    (float('-inf'), 20, 'overly_negative'),
    (20, 45, 'somewhat_negative'),
    (45, 55, 'neutral'),
    (55, 80, 'positive'),
    (80, float('inf'), 'overly_positive')
]

SENTIMENT_MESSAGES = {
    'overly_negative': "The sentiment is overly negative. Twitter users are most likely in shorts. (spot sell pressure, futures short pressure)",
    'somewhat_negative': "The sentiment is somewhat negative. Twitter users are most likely just selling, and a few might be shorting. (spot neutral, futures short pressure)",
    'neutral': "The sentiment is mixed. No alpha can be gained from the feed.",
    'positive': "The sentiment is positive. Twitter users are most likely just holding, and a few might be longing.(spot neutral, futures long pressure)",
    'overly_positive': "The sentiment is overly positive. Twitter users are most likely in longs.(spot buy pressure, futures long pressure)"
}
