import spotipy
import os
import spotipy.util as util
from json.decoder import JSONDecodeError
import json
import random

username = "22kpgi2vtrlebcei6eu37db7y"
scope = 'playlist-read-collaborative playlist-modify-private playlist-modify-public playlist-read-private user-modify-playback-state user-read-currently-playing user-read-playback-state user-read-private user-read-email user-library-modify user-library-read user-follow-modify user-follow-read user-read-recently-played user-top-read streaming app-remote-control'

try:

    token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

except:

    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

spotifyObject = spotipy.Spotify(auth=token)
user = spotifyObject.current_user()

playlist_name = 'Surprise Me Playlist'  # for the post-creation page
songs = [] # empty list to store searched songs
randsongs = [] # empty list to store random songs



class surprisePlaylistClass():
    
    def surpriseSearch(self):
        # Search query and results
        searchResults3 = spotifyObject.search('genre:rock', 5, 0, 'track')
        tracks = searchResults3['tracks']['items']

        for x in tracks: #store searched songs in lists
            if x['popularity'] <= 70:
                songs.append(x['uri'])
                # print(x['name'])
                # print(x['popularity'])


        # Second Search query and results
        searchResults3 = spotifyObject.search('genre:country', 5, 0, 'track')
        tracks = searchResults3['tracks']['items']

        for x in tracks: #store searched songs in lists
            if x['popularity'] <= 70:
                songs.append(x['uri'])
                # print(x['name'])
                # print(x['popularity'])

        # Third Search query and results
        searchResults3 = spotifyObject.search('genre:electroic+dance', 5, 0, 'track')
        tracks = searchResults3['tracks']['items']

        for x in tracks: #store searched songs in lists
            if x['popularity'] <= 70:
                songs.append(x['uri'])
                # print(x['name'])
                # print(x['popularity'])

        # Fourth Search query and results
        searchResults3 = spotifyObject.search('genre:urban+contemporary', 5, 0, 'track')
        tracks = searchResults3['tracks']['items']

        for x in tracks: #store searched songs in lists
            if x['popularity'] <= 70:
                songs.append(x['uri'])
                # print(x['name'])
                # print(x['popularity'])

        # Fifth Search query and results
        searchResults3 = spotifyObject.search('genre:italian+hip+hop', 5, 0, 'track')
        tracks = searchResults3['tracks']['items']

        for x in tracks: #store searched songs in lists
            if x['popularity'] <= 70:
                songs.append(x['uri'])
                # print(x['name'])
                # print(x['popularity'])

        # Sixth Search query and results
        searchResults3 = spotifyObject.search('genre:bachata', 5, 0, 'track')
        tracks = searchResults3['tracks']['items']

        for x in tracks: #store searched songs in lists
            if x['popularity'] <= 70:
                songs.append(x['uri'])
                # print(x['name'])
                # print(x['popularity'])
            

        
        # Seventh Search query and results
        searchResults3 = spotifyObject.search('genre:indie+pop', 5, 0, 'track')
        tracks = searchResults3['tracks']['items']

        for x in tracks: #store searched songs in lists
            if x['popularity'] <= 70:
                songs.append(x['uri'])
                # print(x['name'])
                # print(x['popularity'])

    def savePlaylist(self):

        for x in range(0,30):
            randsongs.append(songs[random.randint(0,(len(songs) - 1))])     #Fill randsongs list with  30 randomly selected songs from playlist list
        
        newPlaylist = spotifyObject.user_playlist_create(user['id'], 'Spicify Surprise Me')
        playlistId = newPlaylist['id'] #create id for new playlist
        spotifyObject.user_playlist_add_tracks(user['id'], playlistId, randsongs, position=None)

        return playlistId

    
    def showPlaylist(self, passedId):
        playlistUrl = 'https://open.spotify.com/embed/playlist/%s' % (passedId)
        # print(playlistUrl)
        return playlistUrl
