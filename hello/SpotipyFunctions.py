import spotipy
import os
import spotipy.util as util
from json.decoder import JSONDecodeError
import json
from PIL import Image
from io import BytesIO
import requests

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
userId = user['id']
profile_pic = user['images'][0]['url']  # profile pic

def getProfilePic():

    try:
        profile_pic = user['images'][0]['url']  # profile pic

    except: # if user does not have Spotify profile picture display default image
        print("user does not have profile picture")
        response = requests.get("https://images.unsplash.com/photo-1534829178390-5312a631a68e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=375&q=80")
        profile_pic = Image.open(BytesIO(response.content))

    return profile_pic

def presentPlaylists():
    myPlaylists = spotifyObject.current_user_playlists()['items']
    playlistList = []

    for i in range(0,len(myPlaylists)):
        playlistList.append(myPlaylists[i]['name'])
    return playlistList


def ratePlaylists(rating):

    newPlaylistId = spotifyObject.current_user_playlists()['items'][0]['id']
    myPlaylists = spotifyObject.current_user_playlists()['items']
    playlistList = []

    for i in range(0,len(myPlaylists)):
        playlistList.append(myPlaylists[i]['name'])
    print(playlistList[0])

    spotifyObject.user_playlist_change_details(user=userId, playlist_id=newPlaylistId, name=(playlistList[0] + " (" + rating + ")"), public=None, collaborative=None, description=None)






