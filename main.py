import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import time
from datetime import datetime
import csv

redirectURI = "http://localhost:8888/callback"
scope = 'user-read-recently-played'


def getCreds():
    load_dotenv()
    clientID = os.getenv("SPOTIFY_CLIENT_ID")
    clientSecret = os.getenv("SPOTIFY_CLIENT_SECRET")
    
    return clientID, clientSecret


if __name__ == "__main__":
    clientID, clientSecret = getCreds()
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=clientID,
    client_secret=clientSecret,
    redirect_uri=redirectURI,
    scope=scope
    ))
    latestTrack = None
    while True:
        results = sp.current_user_recently_played(limit=1)
        if results['items']:
            track = results['items'][0]['track']
            trackName = track['name']
            trackArtist = ', '.join([artist['name'] for artist in track['artists']])
            trackPlayedAt = datetime.strptime(results['items'][0]['played_at'], "%Y-%m-%dT%H:%M:%S.%fZ")
            popScore = track['popularity']
        
        if latestTrack != trackName:
            if not os.path.exists("spotilog.csv"):
                with open("spotilog.csv", 'a', newline='') as spotilog:
                    writer = csv.writer(spotilog)
                    writer.writerow(["Date & Time","Track","Artist","Popularity Score"])

            with open("spotilog.csv", 'a', newline='') as spotilog:
                writer = csv.writer(spotilog)
                writer.writerow([trackPlayedAt,trackName,trackArtist,popScore])
            latestTrack = trackName
            
        time.sleep(30)