"""Script that gets Twitter data based on Tags"""
import tweepy
import csv
import pandas as pd
import datetime
import time

consumer_key = "9YU0fKlZyWFamQduamHXgiyBK"
consumer_secret = "PwgbkX63q25MRsq09081zcvvdXh7l6CQUnOrGay8DCQzfXtoJI"

access_token = "922909274778546176-MNrLhAiu2iKgVWk91vUiDKIt6mQz2ds"
access_token_secret = "Hpa7llr5WrKPbNrp74XlMDlsMr5AOGm4upaXpWh7rNHCo"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#Get Tweets from current till 2018/01/01, write into a DataFrame then convert into a CSV
df = pd.DataFrame({'tag_used_for_tweepy': [], 'date_created': [], 'tweet': [], 'hashtags':[], 'retweets': [], 'likes': []})
hashtags = ["#stockmarket", "#stocks", "#stock", "#trading", "#market", "#news", "#investing", "#finance", "#alpha", "#equity",
            "#business", "#analysis", "#forex", "#trader", "#wallstreet", "#investment"]

for tag in hashtags:
    for tweet in tweepy.Cursor(api.search, q=tag, lang= "en", since= "2018-01-01").items(100000):
        #print (tag, tweet.created_at, tweet.text, tweet.entities.get('hashtags'), tweet.retweet_count, tweet.favorite_count)
        tweet_data = {'tag_used_for_tweepy': tag, 'date_created': tweet.created_at, 'tweet': tweet.text,
                      'hashtags': tweet.entities.get('hashtags'), 'retweets': tweet.retweet_count, 'likes': tweet.favorite_count}
        print(tweet_data)
        df = df.append(tweet_data, ignore_index=True)

#Convert to CSV
df.to_csv(r"/work/lxu/power2323/datamining/twitter_data.csv", header=True, index=False, encoding='utf-8')


