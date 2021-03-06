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

playlist_name = 'Study Playlist'  # for the post-creation page
tracks_name = [] # empty list for track names
tracks_uri = [] # empty list for track uris
selectedStudyTracks_uri = [] # empty list to store songs for Study playlist
randsongs = [] # empty list to store random songs

# Search query and results
searchResults2 = spotifyObject.search('genre:jazz+indie', 50, 0, 'track')
tracks = searchResults2['tracks']['items']

for x in tracks: #store searched songs in lists
    if 70 >= x['popularity']:
            tracks_uri.append(x['uri'])
    #print(x['name'])


# Second Search query and results
searchResults2 = spotifyObject.search('genre:classical', 50, 0, 'track')
tracks = searchResults2['tracks']['items']

for x in tracks: #store searched songs in lists
    if 70 >= x['popularity']:
        tracks_uri.append(x['uri'])
        #print(x['name'])

# Third Search query and results
searchResults2 = spotifyObject.search('genre:chill+piano', 50, 0, 'track')
tracks = searchResults2['tracks']['items']

for x in tracks: #store searched songs in lists
    if 70 >= x['popularity']:
        tracks_uri.append(x['uri'])
        #print(x['name'])

class studyPlaylistClass():


    def studyTracks_uri(self):
        for tracks in tracks_uri: #look through searched tracks uri
            selected_tracks_data = spotifyObject.audio_features(tracks) #get audio features of searched track
            for track_data in selected_tracks_data:
                if 0.0 <= track_data['energy'] <= 0.8:
                    selectedStudyTracks_uri.append(track_data['uri'])
                elif 0.0 <= track_data['speechiness'] <= 1.0:
                    selectedStudyTracks_uri.append(track_data['uri'])
                elif 0.0 <= track_data['loudness'] <= 1.0:
                    selectedStudyTracks_uri.append(track_data['uri'])

        # for x in selectedStudyTracks_uri:
        #     print(x)
        return selectedStudyTracks_uri
        
   
    def savePlaylist(self):
        # global playlistId

        for x in range(0,30):
            randsongs.append(selectedStudyTracks_uri[random.randint(0,(len(selectedStudyTracks_uri) - 1))])     #Fill randsongs list with  30 randomly selected songs from playlist list
        
        newPlaylist = spotifyObject.user_playlist_create(user['id'], 'Spicify Study')
        playlistId = newPlaylist['id'] #create id for new playlist
        spotifyObject.user_playlist_add_tracks(user['id'], playlistId, randsongs, position=None)
        
        return playlistId

    def showPlaylist(self, passedId):
        playlistUrl = 'https://open.spotify.com/embed/playlist/%s' % (passedId)
        return playlistUrl
        


# studyObject = studyPlaylist
# studyObject.studyPlaylist()
# passId = studyObject.savePlaylist()
# studyObject.showPlaylist(passId)