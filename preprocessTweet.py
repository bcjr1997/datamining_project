import csv
import textblob
import utility
import pandas as pd

dataframe = pd.read_csv('twitter_data_100000_financial.csv')

#Preprocess data using Sentiment Analysis of Tweets with TextBlob
output_arr = []
polarity_arr = []
for tweet in dataframe['tweet']:
    output, polarity = utility.get_tweet_text_sentiment(tweet)
    output_arr.append(output)
    polarity_arr.append(polarity)

dataframe['SentimentValue'] = output_arr
dataframe['Polarity'] = polarity_arr

dataframe.to_csv("preprocessedTweet.csv", encoding="utf-8")