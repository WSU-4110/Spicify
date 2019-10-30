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

#22kpgi2vtrlebcei6eu37db7y

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

def beginPlaylist():
    spotifyObject.start_playback(device_id=deviceID, context_uri=Playlists)

def thirtiesPlaylist():

    spotifyObject.user_playlist_create(user['id'], '1930s Playlist')
    newPlaylist = spotifyObject.current_user_playlists()['items'][0]['id']          #Create new empty playlist
    newPlaylistUri = spotifyObject.current_user_playlists()['items'][0]['uri']

    songs = []
    randsongs = []      #Empty Arrays to store songs

    searchResults = spotifyObject.search('1930s music', 1, 0, 'playlist')   #search for music

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']  #Get playlists and playlist owners from search results

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])  #fill playlist list with all songs from search results

    searchResults = spotifyObject.search('1930s nostalgia', 1, 0, 'playlist')       #Do another search for additional songs and veriety

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])  #Add more songs to playlist list

    for x in range(0,29):
        randsongs.append(songs[random.randint(0,(len(songs) - 1))])     #Fill randsongs list with  30 randomly selected songs from playlist list

    spotifyObject.user_playlist_add_tracks(user=userId, playlist_id=newPlaylist, tracks=randsongs)  #Fill playlist with songs from randsongs list

def fourtiesPlaylist():

    spotifyObject.user_playlist_create(user['id'], '1940s Playlist')            #The following functions are the same but with different search queries. 
    newPlaylist = spotifyObject.current_user_playlists()['items'][0]['id']
    newPlaylistUri = spotifyObject.current_user_playlists()['items'][0]['uri']

    songs = []
    randsongs = []

    searchResults = spotifyObject.search('1940s Music - Vocal Hits of the 1940s', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])

    for x in range(0,29):
        randsongs.append(songs[random.randint(0,(len(songs) - 1))])
    print (len(songs))
    print (len(randsongs))

    spotifyObject.user_playlist_add_tracks(user=userId, playlist_id=newPlaylist, tracks=randsongs)

def fiftiesPlaylist():

    spotifyObject.user_playlist_create(user['id'], '1950s Playlist')
    newPlaylist = spotifyObject.current_user_playlists()['items'][0]['id']
    newPlaylistUri = spotifyObject.current_user_playlists()['items'][0]['uri']

    songs = []
    randsongs = []

    searchResults = spotifyObject.search('1950s music', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])

    for x in range(0,29):
        randsongs.append(songs[random.randint(0,(len(songs) - 1))])
    print(playlistUser)

    spotifyObject.user_playlist_add_tracks(user=userId, playlist_id=newPlaylist, tracks=randsongs)

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

def millennialPlaylist():

    spotifyObject.user_playlist_create(user['id'], '2000s Playlist')
    newPlaylist = spotifyObject.current_user_playlists()['items'][0]['id']
    newPlaylistUri = spotifyObject.current_user_playlists()['items'][0]['uri']

    songs = []
    randsongs = []

    searchResults = spotifyObject.search('2000s smash hits', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])

    searchResults = spotifyObject.search('2000s hip hop', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])

    for x in range(0,29):
        randsongs.append(songs[random.randint(0,(len(songs) - 1))])

    spotifyObject.user_playlist_add_tracks(user=userId, playlist_id=newPlaylist, tracks=randsongs)

def returnPlaylists():
    myPlaylists = spotifyObject.current_user_playlists()['items']

    playlistList = []
    
    for i in range(0,len(myPlaylists)):
        playlistList.append(myPlaylists[i]['name'])
    return playlistList



#print(json.dumps(Variable, sort_keys=True, indent=4))