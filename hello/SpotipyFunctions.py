import spotipy
import os
import spotipy.util as util
from json.decoder import JSONDecodeError
import json

username = input("Username: ")
scope = 'user-library-read playlist-modify-public'
try:

    token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

except:

    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

spotifyObject = spotipy.Spotify(auth=token)


user = spotifyObject.current_user()
displayname = user['display_name']
followers = user['followers']['total']


print("Welcome to Spicify " + displayname, "!")
print("You have " + str(followers) + " followers.")

# getting user's playlists

# import pprint
# import sys
# import os
# import subprocess


# token = util.prompt_for_user_token(username)

# if token:
#     sp = spotipy.Spotify(auth=token)
#     playlists = sp.user_playlists(username)
#     for playlist in playlists['items']:
#         print(playlist['name'])
# else:
#     print("Can't get token for", username)
