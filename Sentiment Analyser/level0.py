# level 0, words from level 1 get sent to it, for it to asses whether every single word is positive or negative 

positive_words = [
    'profit', 'bullish', 'gain', 'rally', 'increase', 'uptrend', 'surge', 'rocket',
    'soar', 'rise', 'boom', 'breakout', 'bull', 'growth', 'positive', 'recover', 'recovery',
    'up', 'strong', 'beat', 'advance', 'improve', 'expansion', 'skyrocket', 'all-time high',
    'peak', 'record', 'high', 'buy', 'support', 'favorable', 'optimism', 'success',
    'win', 'green', 'bounce', 'rebound', 'potential', 'prosperity', 'appreciate',
    'solid', 'steady', 'bull run', 'buying pressure', 'upward', 'positive outlook', 'increase in value'
]

negative_words = [
    'loss', 'bearish', 'decline', 'drop', 'decrease', 'downtrend', 'plunge', 'crash',
    'fall', 'slump', 'recession', 'bear', 'negative', 'sell', 'dump', 'panic', 'fear',
    'down', 'weak', 'miss', 'sell-off', 'collapse', 'deteriorate', 'correction', 'low',
    'bottom', 'bear market', 'resistance', 'unfavorable', 'pessimism', 'failure', 'lose',
    'red', 'dip', 'sell pressure', 'pullback', 'losses', 'bearish outlook', 'depreciate',
    'poor', 'volatile', 'bear run', 'downward', 'negative outlook', 'decrease in value', 'negatively'
]

def calculate_sentiment(text):
    words = text.lower().split()
    positive_score = sum(word in positive_words for word in words)
    negative_score = sum(word in negative_words for word in words)
    sentiment_score = positive_score - negative_score
    return sentiment_score
