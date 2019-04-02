import csv
import textblob
import utility

tweet_arr = []
with open("twitter_data_100000_financial.csv") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        tweet_arr.append(row)

#Preprocess data using Sentiment Analysis of Tweets with TextBlob
sentiment_values = {}
for tweet in tweet_arr:
    output = utility.get_tweet_text_sentiment(tweet['tweet'])
    sentiment_values[tweet['tweet']] =  output

