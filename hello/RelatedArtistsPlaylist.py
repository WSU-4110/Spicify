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


randsongs = []  # empty list to store songs that will go into playlist
songs = []      # empty list to store songs from related artists

class relatedArtistsPlaylistClass():

    def unclepostyPlaylist(self):
        searchResults = spotifyObject.search('Post+Malone', 1, 0, 'artist')     # search for selected artist object
        getArtist = searchResults['artists']['items'][0]
        artistId = getArtist['id']          # get slected artist's Id

        relatedArtists = spotifyObject.artist_related_artists(artistId)
        artists = relatedArtists['artists']     # search for related artists

        for x in artists:
            artistName = (x['name'])
            artistSearch = spotifyObject.search(artistName, 2, 0 ,'track')      # search all related artists
            tracks = artistSearch['tracks']['items']
            for x in tracks:
                songs.append(x['uri'])                                          # get songs by realted artists
                # print(songs)
    


    def selenagomezPlaylist(self):
        searchResults = spotifyObject.search('Selena+Gomez', 1, 0, 'artist')     # search for selected artist object
        getArtist = searchResults['artists']['items'][0]
        artistId = getArtist['id']          # get slected artist's Id

        relatedArtists = spotifyObject.artist_related_artists(artistId)
        artists = relatedArtists['artists']     # search for related artists

        for x in artists:
            artistName = (x['name'])
            artistSearch = spotifyObject.search(artistName, 2, 0 ,'track')      # search all related artists
            tracks = artistSearch['tracks']['items']
            for x in tracks:
                songs.append(x['uri'])                                          # get songs by related artists
                # print(songs)
    

    
    def rezzPlaylist(self):
        searchResults = spotifyObject.search('Rezz', 1, 0, 'artist')     # search for selected artist object
        getArtist = searchResults['artists']['items'][0]
        artistId = getArtist['id']          # get slected artist's Id

        relatedArtists = spotifyObject.artist_related_artists(artistId)
        artists = relatedArtists['artists']     # search for related artists

        for x in artists:
            artistName = (x['name'])
            artistSearch = spotifyObject.search(artistName, 2, 0 ,'track')      # search all related artists
            tracks = artistSearch['tracks']['items']
            for x in tracks:
                songs.append(x['uri'])                                          # get songs by related artists
                # print(songs)
    


    def atribecalledquestPlaylist(self):
        searchResults = spotifyObject.search('A+Tribe+Called+Quest', 1, 0, 'artist')     # search for selected artist object
        getArtist = searchResults['artists']['items'][0]
        artistId = getArtist['id']          # get slected artist's Id

        relatedArtists = spotifyObject.artist_related_artists(artistId)
        artists = relatedArtists['artists']     # search for related artists

        for x in artists:
            artistName = (x['name'])
            artistSearch = spotifyObject.search(artistName, 2, 0 ,'track')      # search all related artists
            tracks = artistSearch['tracks']['items']
            for x in tracks:
                songs.append(x['uri'])                                          # get songs by related artists
                # print(songs)
    


    def travisscottPlaylist(self):
        searchResults = spotifyObject.search('Travis+Scott', 1, 0, 'artist')     # search for selected artist object
        getArtist = searchResults['artists']['items'][0]
        artistId = getArtist['id']          # get slected artist's Id

        relatedArtists = spotifyObject.artist_related_artists(artistId)
        artists = relatedArtists['artists']     # search for related artists

        for x in artists:
            artistName = (x['name'])
            artistSearch = spotifyObject.search(artistName, 2, 0 ,'track')      # search all related artists
            tracks = artistSearch['tracks']['items']
            for x in tracks:
                songs.append(x['uri'])                                          # get songs by related artists
                # print(songs)
    

    def timmcgrawPlaylist(self):
        searchResults = spotifyObject.search('Tim+McGraw', 1, 0, 'artist')     # search for selected artist object
        getArtist = searchResults['artists']['items'][0]
        artistId = getArtist['id']          # get slected artist's Id

        relatedArtists = spotifyObject.artist_related_artists(artistId)
        artists = relatedArtists['artists']     # search for related artists

        for x in artists:
            artistName = (x['name'])
            artistSearch = spotifyObject.search(artistName, 2, 0 ,'track')      # search all related artists
            tracks = artistSearch['tracks']['items']
            for x in tracks:
                songs.append(x['uri'])                                          # get songs by related artists
                # print(songs)


    def nancyajramPlaylist(self):
        searchResults = spotifyObject.search('Nancy+Ajram', 1, 0, 'artist')     # search for selected artist object
        getArtist = searchResults['artists']['items'][0]
        artistId = getArtist['id']          # get slected artist's Id

        relatedArtists = spotifyObject.artist_related_artists(artistId)
        artists = relatedArtists['artists']     # search for related artists

        for x in artists:
            artistName = (x['name'])
            artistSearch = spotifyObject.search(artistName, 2, 0 ,'track')      # search all related artists
            tracks = artistSearch['tracks']['items']
            for x in tracks:
                songs.append(x['uri'])                                          # get songs by related artists
                # print(songs)


    def princePlaylist(self):
        searchResults = spotifyObject.search('Prince', 5, 0, 'artist')     # search for selected artist object
        getArtist = searchResults['artists']['items'][1]
        artistId = getArtist['id']          # get slected artist's Id

        relatedArtists = spotifyObject.artist_related_artists(artistId)
        artists = relatedArtists['artists']     # search for related artists

        for x in artists:
            artistName = (x['name'])
            # print(artistName)
            artistSearch = spotifyObject.search(artistName, 2, 0 ,'track')      # search all related artists
            tracks = artistSearch['tracks']['items']
            for x in tracks:
                songs.append(x['uri'])                                          # get songs by related artists
                # print(songs)

   
    def savePlaylist(self):

        for x in range(0,30):
            randsongs.append(songs[random.randint(0,(len(songs) - 1))])     #Fill randsongs list with  30 randomly selected songs from playlist list
        
        newPlaylist = spotifyObject.user_playlist_create(user['id'], 'Spicify Related Artist')
        playlistId = newPlaylist['id'] #create id for new playlist
        spotifyObject.user_playlist_add_tracks(user['id'], playlistId, randsongs, position=None)

        return playlistId

    def showPlaylist(self, passedId):
        playlistUrl = 'https://open.spotify.com/embed/playlist/%s' % (passedId)
        return playlistUrl


raObject = relatedArtistsPlaylistClass()
raObject.princePlaylist()