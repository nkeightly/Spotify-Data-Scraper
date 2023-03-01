import pandas as pd
import matplotlib.pyplot as plt

# Load the scraped data into pandas dataframes
playlist_df = pd.read_csv('data/playlists.csv')
song_df = pd.read_csv('data/songs.csv')
artist_df = pd.read_csv('data/artists.csv')

# Group the data by artist and get the mean popularity score for each artist
artist_popularity = artist_df.groupby('artist')['popularity'].mean()

# Sort the data in descending order of popularity and plot a bar chart
artist_popularity_sorted = artist_popularity.sort_values(ascending=False)
artist_popularity_sorted.plot(kind='bar

# Sort the data in ascending order of popularity and plot a bar chart
#Edit>>
artist_popularity_sorted = artist_popularity.sort_values(descending=False)
artist_popularity_sorted.plot(kind='bar
