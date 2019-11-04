import spotipy
import os
import spotipy.util as util
from json.decoder import JSONDecodeError
import json

username = '22kpgi2vtrlebcei6eu37db7y'
scope = 'user-library-read playlist-modify-public'
try:

    token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

except:

    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

spotifyObject = spotipy.Spotify(auth=token)


# user info
user = spotifyObject.current_user()
displayname = user['display_name'] # name
followers = user['followers']['total'] # followers
profile_pic = user['images'][0]['url']  # profile pic


# print("Welcome to Spicify " + displayname, "!")
# print("You have " + str(followers) + " followers.")

