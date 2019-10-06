import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError


username = "22kpgi2vtrlebcei6eu37db7y"
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

#Easily Install the latest version of spotipy for playback functions:
#pip install git+https://github.com/plamere/spotipy.git --upgrade 

# 22kpgi2vtrlebcei6eu37db7y

try:

    token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

except:

    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

spotifyObject = spotipy.Spotify(auth=token)

devices = spotifyObject.devices()
deviceID = devices['devices'][0]['id']

user = spotifyObject.current_user()
displayname = user['display_name']
followers = user['followers']['total']

Playlists = spotifyObject.current_user_playlists()['items'][0]['uri']

def beginPlaylist():
    spotifyObject.start_playback(device_id=deviceID, context_uri=Playlists)

beginPlaylist()
