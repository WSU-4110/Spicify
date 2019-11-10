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

playlist_name = 'Workout playlist'  # for the post-creation page
tracks_name = [] #empty list for track names
tracks_uri = [] #empty list for track uris
selectedWorkoutTracks_uri = [] # empty list to store songs for workout playlist
randsongs = [] # empty list to store random songs

# Search query and results
searchResults = spotifyObject.search('genre:crunk+pop', 50, 0, 'track')
tracks = searchResults['tracks']['items']

# store seached songs in list
for x in tracks:
    if x['popularity'] <= 70:
        tracks_uri.append(x['uri'])
        #print(x['name']) # testing purpose

# Second search to gather even more songs
searchResults = spotifyObject.search('genre:southern+hip+hop', 50, 0 , 'track')
tracks = searchResults['tracks']['items']

# store seached songs in list
for x in tracks:
    if x['popularity'] <= 70:
        tracks_uri.append(x['uri'])
        #print(x['name']) # testing purpose

# Third search to gather even more songs
searchResults = spotifyObject.search('genre:pop+rock', 50, 0 , 'track')
tracks = searchResults['tracks']['items']

# store seached songs in list
for x in tracks:
    if x['popularity'] <= 70:
        tracks_uri.append(x['uri'])
        #print(x['name']) # testing purpose

# Fourth search to gather even more songs
searchResults = spotifyObject.search('genre:dance+pop+rave', 50, 0 , 'track')
tracks = searchResults['tracks']['items']

# store seached songs in list
for x in tracks:
    if x['popularity'] <= 70:
        tracks_uri.append(x['uri'])
        #print(x['name']) # testing purpose

# for x in tracks:
#     print(x['name'])
#     print(x['popularity'])
# print(tracks)

# abstract class 
class Playlist():
    # @abc.abstractclassmethod
    def generateURIs():
        pass
    
    # @abc.abstractclassmethod
    def savePlaylist():
        pass

    # @abc.abstractclassmethod
    def showPlaylist():
        pass
 

class workoutPlaylistClass(Playlist):
    
    # function to narrorw down search to match our workout sound attributes
    def generateURIs(self):
        for tracks in tracks_uri: #look through searched tracks uri
            selected_tracks_data = spotifyObject.audio_features(tracks) #get audio features of searched track
            for track_data in selected_tracks_data:
                if 0.7 <= track_data['energy'] <= 1.0:
                    selectedWorkoutTracks_uri.append(track_data['uri'])
                elif 50 <= track_data['tempo'] <= 200:
                    selectedWorkoutTracks_uri.append(track_data['uri'])
                elif 0.7 <= track_data['valence'] <= 1.0:
                    selectedWorkoutTracks_uri.append(track_data['uri'])


        return selectedWorkoutTracks_uri


    def savePlaylist(self):

        for x in range(0,30):
            randsongs.append(selectedWorkoutTracks_uri[random.randint(0,(len(selectedWorkoutTracks_uri) - 1))])     #Fill randsongs list with  30 randomly selected songs from playlist list
        
        newPlaylist = spotifyObject.user_playlist_create(user['id'], 'Spicify Workout')
        playlistId = newPlaylist['id'] #create id for new playlist
        spotifyObject.user_playlist_add_tracks(user['id'], playlistId, randsongs, position=None)

        return playlistId

    def showPlaylist(self, passedId):
        playlistUrl = 'https://open.spotify.com/embed/playlist/%s' % (passedId)
        return playlistUrl


class PlaylistFactory(Playlist):

    def CreatePlaylist(self, playListType):
        playListToCreate = None
        if(playListType == "workout"):
            playListToCreate = workoutPlaylistClass()
        return playListToCreate


        

