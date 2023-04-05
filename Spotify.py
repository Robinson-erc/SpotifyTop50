import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt

# Set up Spotify API client credentials
client_id = "e9fb00b2739c4107843e3cd0fb2e4cef"
client_secret = "47be381b7b7740d699d088fc36ddcf26"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Define the Genre
query = "genre:hip-hop"

# Retrieve the top 50 hip-hop tracks
results = sp.search(q=query, type="track", limit=50)
top_tracks = results["tracks"]["items"]

# Extract the track names and popularity scores
names = [f"{track['artists'][0]['name']} - {track['name']}" for track in top_tracks]
popularity = [track["popularity"] for track in top_tracks]

# Create a bar graph of the top 50 hip-hop tracks
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
ax1.bar(names, popularity, color="red")
ax1.set_title("Top 50 Hip-Hop Tracks on Spotify (Bar Graph)")
ax1.set_xlabel("Track")
ax1.set_ylabel("Popularity")
ax1.set_xticklabels(names, rotation=90)

# Create a line graph of the top 50 hip-hop tracks
ax2.plot(names, popularity, color="blue")
ax2.set_title("Top 50 Hip-Hop Tracks on Spotify (Line Graph)")
ax2.set_xlabel("Track")
ax2.set_ylabel("Popularity")
ax2.set_xticklabels(names, rotation=90)

plt.show()
