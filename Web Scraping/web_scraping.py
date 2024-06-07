import requests
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import re

# We are downloading the Vader lexicon, which will indicate the general sentiment polarity and intensity of the words.
nltk.download('vader_lexicon')

# Listing the words that should be analysed
words = [
    'profit', 'bullish', 'gain', 'rally', 'increase', 'uptrend', 'surge', 'rocket',
    'soar', 'rise', 'boom', 'breakout', 'bull', 'growth', 'positive', 'recover', 'recovery',
    'up', 'strong', 'beat', 'advance', 'improve', 'expansion', 'skyrocket', 'all-time high',
    'peak', 'record', 'high', 'buy', 'support', 'favorable', 'optimism', 'success',
    'win', 'green', 'bounce', 'rebound', 'potential', 'prosperity', 'appreciate',
    'solid', 'steady', 'bull run', 'buying pressure', 'upward', 'positive outlook', 'increase in value','loss', 'bearish', 'decline', 'drop', 'decrease', 'downtrend', 'plunge', 'crash',
    'fall', 'slump', 'recession', 'bear', 'negative', 'sell', 'dump', 'panic', 'fear',
    'down', 'weak', 'miss', 'sell-off', 'collapse', 'deteriorate', 'correction', 'low',
    'bottom', 'bear market', 'resistance', 'unfavorable', 'pessimism', 'failure', 'lose',
    'red', 'dip', 'sell pressure', 'pullback', 'losses', 'bearish outlook', 'depreciate',
    'poor', 'volatile', 'bear run', 'downward', 'negative outlook', 'decrease in value', 'negatively', 'blood'
]

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Scrape news articles from Bloomberg
def scrape_bloomberg():
    url = 'https://www.bloomberg.com/markets'
    articles = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    for item in soup.find_all('article'):
        if item.find('h3'):
            link = item.find('a', href=True)['href']
            if not link.startswith('http'):
                link = 'https://www.bloomberg.com' + link
            article_text = scrape_article_text(link)
            if article_text:
                articles.append(article_text)
    
    return articles

# Scrape news articles from CNBC
def scrape_cnbc():
    url = 'https://www.cnbc.com/world/?region=world'
    articles = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    for item in soup.find_all('a', {'class': 'Card-title'}):
        link = item['href']
        if not link.startswith('http'):
            link = 'https://www.cnbc.com' + link
        article_text = scrape_article_text(link)
        if article_text:
            articles.append(article_text)
    
    return articles

# Scrape the text content of an article
def scrape_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    article_text = ' '.join([para.get_text() for para in paragraphs])
    return article_text if article_text else None

# Combines all articles 
def scrape_financial_articles():
    articles = []
    articles.extend(scrape_bloomberg())
    articles.extend(scrape_cnbc())
    return articles

# A function to analyze word usage sentiment
def analyze_word_usage(words, articles):
    word_counts = {word: {'bullish': 0, 'bearish': 0} for word in words}
    
    for article in articles:
        sentences = re.split(r'\.|\?', article)
        for sentence in sentences:
            sentiment_score = sia.polarity_scores(sentence)['compound']
            for word in words:
                if word in sentence:
                    if sentiment_score > 0:
                        word_counts[word]['bullish'] += 1
                    elif sentiment_score < 0:
                        word_counts[word]['bearish'] += 1
    
    return word_counts

# Scraping articles from financial news websites
articles = scrape_financial_articles()

# Analyzing word usage in the articles
word_counts = analyze_word_usage(words, articles)

# Calculating probabilities
word_probabilities = {}
for word, counts in word_counts.items():
    total_occurrences = counts['bullish'] + counts['bearish']
    if total_occurrences > 0:
        word_probabilities[word] = counts['bullish'] / total_occurrences
    else:
        word_probabilities[word] = None  # No occurrences found

# Print the probabilities
for word, probability in word_probabilities.items():
    if probability is not None:
        print(f"The word '{word}' has a bullish probability of {probability:.2f}")
    else:
        print(f"The word '{word}' did not appear in the articles")