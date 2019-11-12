import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
import random

username = '22kpgi2vtrlebcei6eu37db7y'
scope = 'playlist-read-collaborative playlist-modify-private playlist-modify-public playlist-read-private user-modify-playback-state user-read-currently-playing user-read-playback-state user-read-private user-read-email user-library-modify user-library-read user-follow-modify user-follow-read user-read-recently-played user-top-read streaming app-remote-control'

try:

    token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

except:

    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

spotifyObject = spotipy.Spotify(auth=token)     # create object of type spotipy
user = spotifyObject.current_user()             # get current app user


class relatedArtistsPlaylistClass():

    def unclepostyPlaylist(self):
        
        searchResults = spotifyObject.search('artist:Post+Malone', 1, 0, 'artist')
        print(searchResults)
        # getArtist = searchResults['artist']['items'][0]['id']
        
        # # store seached songs in list
        # for x in getArtist:
        #     artistId.append(x['id'])
        # print(artistId)

raObj = relatedArtistsPlaylistClass()
raObj.unclepostyPlaylist()


