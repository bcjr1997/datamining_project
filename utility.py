"""File contains methods for this project"""
from textblob import TextBlob
import tweepy
import csv

def get_tweet_text_sentiment(tweet_text):
    analyse_tweet = TextBlob(tweet_text)
    if analyse_tweet.sentiment.polarity > 0:
        return "Positive", analyse_tweet.sentiment.polarity
    elif analyse_tweet.sentiment.polarity == 0:
        return "Neutral", analyse_tweet.sentiment.polarity
    else:
        return "Negative", analyse_tweet.sentiment.polarity