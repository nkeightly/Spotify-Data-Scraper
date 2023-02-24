import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Initialize Spotify API credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Define playlists, songs, and artists to scrape data from
playlists = ['37i9dQZEVXbMDoHDwVN2tF', '37i9dQZF1DXcBWIGoYBM5M']
songs = ['4sLtOBOzn4s3GDUv3c5oJD', '6Sj7V0WJ3u3aDZT0P7ryiz']
artists = ['1uNFoZAHBGtllmzznpCI3s', '3TVXtAsR1Inumwj472S9r4']

# Scrape data from playlists
playlist_data = []
for playlist in playlists:
    results = sp.playlist(playlist, fields="tracks")
    tracks = results['tracks']
    for item in tracks['items']:
        track = item['track']
        # Extract relevant data from track and store in list
        playlist_data.append({
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'popularity': track['popularity'],
            'album': track['album']['name'],
            'playlist': playlist
        })

# Scrape data from songs
song_data = []
for song in songs:
    results = sp.track(song)
    # Extract relevant data from song and store in list
    song_data.append({
        'name': results['name'],
        'artist': results['artists'][0]['name'],
        'popularity': results['popularity'],
        'album': results['album']['name']
    })

# Scrape data from artists
artist_data = []
for artist in artists:
    results = sp.artist_top_tracks(artist)
    tracks = results['tracks']
    for track in tracks:
        # Extract relevant data from track and store in list
        artist_data.append({
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'popularity': track['popularity'],
            'album': track['album']['name']
        })

# Save data to CSV files
playlist_df = pd.DataFrame(playlist_data)
playlist_df.to_csv('data/playlists.csv', index=False)

song_df = pd.DataFrame(song_data)
song_df.to_csv('data/songs.csv', index=False)

artist_df = pd.DataFrame(artist_data)
artist_df.to_csv('data/artists.csv', index=False)
