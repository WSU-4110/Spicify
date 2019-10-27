import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
import random


username = '22kpgi2vtrlebcei6eu37db7y'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

#22kpgi2vtrlebcei6eu37db7y

#Easily Install the latest version of spotipy for playback functions:
#pip install git+https://github.com/plamere/spotipy.git --upgrade 

try:

    token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

except:

    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

spotifyObject = spotipy.Spotify(auth=token)


user = spotifyObject.current_user()
displayname = user['display_name']
followers = user['followers']['total']
userId = user['id']

devices = spotifyObject.devices()
deviceID = devices['devices'][0]['id']

Playlists = spotifyObject.current_user_playlists()['items'][0]['uri']


def beginPlaylist():
    spotifyObject.start_playback(device_id=deviceID, context_uri=Playlists)

def thirtiesPlaylist():

    spotifyObject.user_playlist_create(user['id'], '1930s Playlist')
    newPlaylist = spotifyObject.current_user_playlists()['items'][0]['id']
    newPlaylistUri = spotifyObject.current_user_playlists()['items'][0]['uri']

    songs = []
    randsongs = []

    searchResults = spotifyObject.search('1930s music', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])

    searchResults = spotifyObject.search('1930s nostalgia', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])

    for x in range(0,29):
        randsongs.append(songs[random.randint(0,(len(songs) - 1))])

    spotifyObject.user_playlist_add_tracks(user=userId, playlist_id=newPlaylist, tracks=randsongs)
    spotifyObject.start_playback(device_id=deviceID, context_uri=newPlaylistUri)

def sixtiesPlaylist():

    spotifyObject.user_playlist_create(user['id'], '1960s Playlist')
    newPlaylist = spotifyObject.current_user_playlists()['items'][0]['id']
    newPlaylistUri = spotifyObject.current_user_playlists()['items'][0]['uri']

    songs = []
    randsongs = []

    searchResults = spotifyObject.search('1960s music', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])

    searchResults = spotifyObject.search('1960s rock', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])

    for x in range(0,29):
        randsongs.append(songs[random.randint(0,(len(songs) - 1))])

    spotifyObject.user_playlist_add_tracks(user=userId, playlist_id=newPlaylist, tracks=randsongs)
    spotifyObject.start_playback(device_id=deviceID, context_uri=newPlaylistUri)

def eightiesPlaylist():

    spotifyObject.user_playlist_create(user['id'], '1980s Playlist')
    newPlaylist = spotifyObject.current_user_playlists()['items'][0]['id']
    newPlaylistUri = spotifyObject.current_user_playlists()['items'][0]['uri']

    songs = []
    randsongs = []

    searchResults = spotifyObject.search('1980s music', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])

    searchResults = spotifyObject.search('80s popped!', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])

    for x in range(0,29):
        randsongs.append(songs[random.randint(0,(len(songs) - 1))])

    spotifyObject.user_playlist_add_tracks(user=userId, playlist_id=newPlaylist, tracks=randsongs)
    spotifyObject.start_playback(device_id=deviceID, context_uri=newPlaylistUri)

def SeventiesPlaylist():

    spotifyObject.user_playlist_create(user['id'], '1970s Playlist')
    newPlaylist = spotifyObject.current_user_playlists()['items'][0]['id']
    newPlaylistUri = spotifyObject.current_user_playlists()['items'][0]['uri']

    songs = []
    randsongs = []

    searchResults = spotifyObject.search('1970s music', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])

    searchResults = spotifyObject.search('70s road trip', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])

    for x in range(0,29):
        randsongs.append(songs[random.randint(0,(len(songs) - 1))])

    spotifyObject.user_playlist_add_tracks(user=userId, playlist_id=newPlaylist, tracks=randsongs)
    spotifyObject.start_playback(device_id=deviceID, context_uri=newPlaylistUri)

def NinetiesPlaylist():

    spotifyObject.user_playlist_create(user['id'], '1990s Playlist')
    newPlaylist = spotifyObject.current_user_playlists()['items'][0]['id']
    newPlaylistUri = spotifyObject.current_user_playlists()['items'][0]['uri']

    songs = []
    randsongs = []

    searchResults = spotifyObject.search('1990s love songs', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])

    searchResults = spotifyObject.search('All out 90s', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])

    for x in range(0,29):
        randsongs.append(songs[random.randint(0,(len(songs) - 1))])

    spotifyObject.user_playlist_add_tracks(user=userId, playlist_id=newPlaylist, tracks=randsongs)
    spotifyObject.start_playback(device_id=deviceID, context_uri=newPlaylistUri)

def returnPlaylists():
    myPlaylists = spotifyObject.current_user_playlists()['items']

    playlistList = []
    
    for i in range(0,len(myPlaylists)):
        playlistList.append(myPlaylists[i]['name'])
        #print(str(myPlaylists[i]['name']))
    return playlistList

eightiesPlaylist()

print(json.dumps(user, sort_keys=True, indent=4))

