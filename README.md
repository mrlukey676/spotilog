# spotilog
Log Spotify activity

## About
I got bored waiting for Spotify Wrapped 2024, so this short program gets the most recent song you've listened to and logs it in a CSV file. Put it on an 'always on' machine so whenever you listen to a song, it logs it!

## How to use
You'll need to make an app on https://developer.spotify.com/ before you can use it. The app can be called whatever you want, as long as the redirect URI is http://localhost:8888/callback. Then, in the same folder and the 'main.py' file, create a file called '.env' and inside, insert the following details:
```
SPOTIFY_CLIENT_ID=YOUR_ID_HERE
SPOTIFY_CLIENT_SECRET=YOUR_SECRET_HERE
```
where 'YOUR_ID_HERE' and 'YOUR_SECRET_HERE' are replaced with the appropriate details from your application you made earlier. After that, you're ready to run the program!

## Coming Soon
- Web Interface (I hope)

Any features you want to see or any weird bugs? Make an issue.