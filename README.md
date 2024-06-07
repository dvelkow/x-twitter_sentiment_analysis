# x-twitter_sentiment_analysis
A financial sentiment analysis dashboard for X/Twitter, mainly aiming to gauge greed/fear level based on tweets for a given ticker.

### It is constructed of 3 levels 
- **Level 2/ Main:** Recieves Tweets from Twitter API, with the selected ticker and sends them to *Level 1* for further analysis.
- **Level 1:** Splits the tweet to different parts, then it sends every word from the part to *Level 0* for further analysis, after it recieves every word's sentiment probability it averages out the score for the given part 
- **Level 0:** Analyses every single word from a tweet and asseses the probability it's negative or positive, and sends the probability value to lvl 1
### Table of Contents
- [Overview](#Overview)
- [IMPORTANT](#Important)
- [How to Use](#how-to-use)
- [Setup Instructions](#approach)

### Overview
This project leverages natural language processing techniques to gauge market sentiment.The project is structured into different levels, each focusing on specific tasks, making it easier to understand, maintain, and extend. It fetches real-time tweets using the Twitter API for live sentiment analysis

### IMPORTANT
Since the system depends on utalising Twitter's API and only a few people have access to it, I have attached a Mock Version to the repository. In it, you can either run it with the mock Tweets or copy paste real tweets to see how it processes them.
Of course, only if you have access to twitter API you can see the full potential of the system.

### How to Use

If ur trying the Mock Version:
   ```bash
   git clone https://github.com/dvelkow/x-twitter_sentiment_analysis
   cd Sentiment Analyser Mock Version
   ```

If ur trying the API accessing Version
   ```bash
   git clone https://github.com/dvelkow/x-twitter_sentiment_analysis
   cd Sentiment Analyser
   ```
### Setup Instructions 
You only need access to Python, in it you can explore all 3 files into a folder and run the 2nd level, just change the variables according to your needs
