import pytest
import spotipy
import os
import spotipy.util as util
from json.decoder import JSONDecodeError
import json
from PIL import Image
from io import BytesIO
import requests

username = "22kpgi2vtrlebcei6eu37db7y"
scope = 'playlist-read-collaborative playlist-modify-private playlist-modify-public playlist-read-private user-modify-playback-state user-read-currently-playing user-read-playback-state user-read-private user-read-email user-library-modify user-library-read user-follow-modify user-follow-read user-read-recently-played user-top-read streaming app-remote-control'

try:

    token = util.prompt_for_user_token(username, scope, client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',
                                       client_secret='03d0e4de0957434abcc60660045d7cfc', redirect_uri='https://www.google.com/')

except:

    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope, client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',
                                       client_secret='03d0e4de0957434abcc60660045d7cfc', redirect_uri='https://www.google.com/')

spotifyObject = spotipy.Spotify(auth=token)
user = spotifyObject.current_user()


def test_workoutTracks_uri():
    spotifyObject = spotipy.Spotify(auth=token)
    user = spotifyObject.current_user()
    tracks_uri = []
    selectedWorkoutTracks_uri = []

    searchResults = spotifyObject.search('genre:crunk+pop', 50, 0, 'track')
    tracks = searchResults['tracks']['items']
    # store seached songs in list
    for x in tracks:
        if x['popularity'] <= 70:
            tracks_uri.append(x['uri'])
            #print(x['name']) # testing purpose

    for tracks in tracks_uri:  # look through searched tracks uri
        selected_tracks_data = spotifyObject.audio_features(
            tracks)  # get audio features of searched track
        for track_data in selected_tracks_data:
            if 0.7 <= track_data['energy'] <= 1.0:
                selectedWorkoutTracks_uri.append(track_data['uri'])
            elif 50 <= track_data['tempo'] <= 200:
                selectedWorkoutTracks_uri.append(track_data['uri'])
            elif 0.7 <= track_data['valence'] <= 1.0:
                selectedWorkoutTracks_uri.append(track_data['uri'])
        assert len(selectedWorkoutTracks_uri) != 0


def test_savePlaylist():

        playlistId = 0
        newPlaylist = spotifyObject.user_playlist_create(
            user['id'], 'Spicify Surprise Me')
        playlistId = newPlaylist['id']  # create id for new playlist

        assert playlistId != 0


def test_studyTracks_uri():
    spotifyObject = spotipy.Spotify(auth=token)
    user = spotifyObject.current_user()
    selectedStudyTracks_uri = []

    searchResults2 = spotifyObject.search('genre:jazz+indie', 50, 0, 'track')
    tracks = searchResults2['tracks']['items']

    assert len(tracks) == 50


def test_surpriseSearch():
    songs = []  # empty list to store searched songs

    # Search query and results
    searchResults3 = spotifyObject.search('genre:rock', 50, 0, 'track')
    tracks = searchResults3['tracks']['items']

    for x in tracks:  # store searched songs in lists
        songs.append(x['uri'])

    assert len(songs) > 2








def test_internationalPlaylist():
        # setting up variables
        spotifyObject.user_playlist_create(user['id'], 'International Playlist')
        newPlaylist = spotifyObject.current_user_playlists()['items'][0]['id']
        newPlaylistUri = spotifyObject.current_user_playlists()['items'][0]['uri']

        songs = []
        randsongs = []

        # functionality
        searchResults = spotifyObject.search('Indian Chill', 1, 0, 'playlist')  # Indian Music

        playlistResult = searchResults['playlists']['items'][0]['id']
        # Get playlists and playlist owners from search results
        playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

        playlist = spotifyObject.user_playlist_tracks(user=playlistUser, playlist_id=playlistResult)
        

        assert(playlist != 0)

def test_drivingTracks_uri():
    tracks = []
    tracks_uri = []
    selectedDrivingTracks_uri = []

    searchResults3 = spotifyObject.search('genre:electro+jazz', 50, 0, 'track')

    tracks = searchResults3['tracks']['items']

    for x in tracks:  # store searched songs in lists
        if x['popularity'] <= 70:
            tracks_uri.append(x['uri'])

    for tracks in tracks_uri: #look through searched tracks uri
        selected_tracks_data = spotifyObject.audio_features(tracks) #get audio features of searched track
        for track_data in selected_tracks_data:
            if 100 <= track_data['tempo'] <= 200:
                selectedDrivingTracks_uri.append(track_data['uri'])
                assert(track_data['tempo'] <= 200)
            elif 0.5 <= track_data['valence'] <= 1.0:
                selectedDrivingTracks_uri.append(track_data['uri'])
                assert(track_data['valence'] <= 1.0)
            elif 0.4 <= track_data['liveness'] <= 1.0:
                selectedDrivingTracks_uri.append(track_data['uri'])
                assert(track_data['liveness'] <= 1.0)
        assert(len(selectedDrivingTracks_uri) > 0)
        

def test_surpriseSearch():
        # Search query and results
        searchResults3 = spotifyObject.search('genre:rock', 5, 0, 'track')
        tracks = searchResults3['tracks']['items']
        songs = []

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
        assert(len(searchResults3) < 6)
        assert(len(songs) >= 0)
        # assert(songs[1]['popularity'] <= 70)
