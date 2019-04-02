import csv
import textblob
import utility
import pandas as pd

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

#Convert Dictionary to Dataframe
df = pd.DataFrame(sentiment_values.items(), columns=["Tweet", "SentimentValue"])
print(df.SentimentValue.unique())