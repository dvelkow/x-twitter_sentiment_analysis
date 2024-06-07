# level 0, words from level 1 get sent to it, for it to asses the probability of every single word being positive 

bullish_probabilities = {
    'gain': 0.78, 'rally': 1.0, 'increase': 0.8, 'surge': 1.0, 'soar': 1.0,
    'rise': 0.44, 'boom': 1.0, 'growth': 1.0, 'positive': 1.0, 'recover': 0.6,
    'recovery': 0.67, 'up': 0.79, 'strong': 0.5, 'beat': 1.0, 'advance': 1.0,
    'improve': 1.0, 'all-time high': 0.67, 'peak': 0.92, 'solid': 0.6, 'FOMO': 0.7,
    'record': 0.43, 'negatively': 0.21, 'fear': 0.3, 'selling': 0.2,
    'high': 0.55, 'buy': 0.85, 'support': 1.0, 'success': 1.0, 'win': 0.76,
    'green': 0.33, 'potential': 0.75, 'appreciate': 1.0, 'solid': 1.0, 'blood': 0.25, 
    'profit': 0.75, 'bullish': 0.75, 'skyrocket': 0.75, 'bounce': 0.75,
    'poor': 0.33, 'lose': 0.67, 'dip': 0.25, 'red': 0.84, 'losses': 0.5, 'miss': 0.43, 
    'bearish': 0.25, 'collapse': 0, 'lose': 0.67, 'downward': 0.25, 'bear': 0.25, 'dip': 0.25,
    'recession': 0.3, 'sell': 0.33, 'negative': 0.23, 'dump': 0.17, 'panic': 0.4, 'fall': 0.15
}

def calculate_sentiment(text):
    words = text.lower().split()
    total_score = 0
    relevant_words = 0

    for word in words:
        if word in bullish_probabilities:
            total_score += bullish_probabilities[word]
            relevant_words += 1

    if relevant_words > 0:
        average_score = total_score / relevant_words
    else:
        average_score = 0.5  # Neutral if no relevant words found

    return average_score