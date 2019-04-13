from sklearn.cluster import KMeans  # Clustering Library
import pandas as pd                 # You can visualize the CSV file using 
import numpy as np

#To load the CSV file 
#This is a DataFrame object
df = pd.read_csv('preprocessedTweet.csv')
#You can visualize the whole csv file using just the print statement
print(df)
#If you want to print a column
print(df['tweet'])