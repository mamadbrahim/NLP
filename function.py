import nltk
from textblob import TextBlob 
from nltk.sentiment import SentimentIntensityAnalyzer

def blob_fun(text):
    # Perform sentiment analysis using TextBlob
    analysis = TextBlob(text)
    # Assign sentiment polarity as positive, negative, or neutral
    return 'positive' if analysis.sentiment.polarity > 0 else 'negative' if analysis.sentiment.polarity < 0 else 'neutral'

def vader_fun(text):
    # nltk.download('vader_lexicon') # execute this line only once
    # Perform sentiment analysis using VADER
    # Initialize VADER sentiment analyzer
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)
    # Assign sentiment polarity as positive, negative, or neutral based on the compound score
    return 'positive' if scores['compound'] >= 0.05 else 'negative' if scores['compound'] <= -0.05 else 'neutral'
