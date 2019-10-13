import spotipy
import os
import spotipy.util as util
from json.decoder import JSONDecodeError
import json

username = input('Username: ')
scope = 'user-library-read playlist-modify-public'

try:

    token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

except:

    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

spotifyObject = spotipy.Spotify(auth=token)


# Search query and results
searchResults = spotifyObject.search('genre:hip+hop+pop'and'year:2007-2016', 50, 0, 'track')
tracks = searchResults['tracks']['items']
# for x in tracks:
#     print(x['name'])
print(tracks)
tracks_name = [] #empty list for track names
tracks_uri = [] #empty list for track uris
selectedWorkoutTracks_uri = [] # empty list to store songs for workout playlist
for x in tracks: #store searched songs in lists
    tracks_name.append(x['name'])
    if  x['popularity'] <= 40:
        tracks_uri.append(x['uri'])

    
# function to narrorw down search to match our workout sound attributes
def workoutTracks_uri(spotifyObject, tracks_uri):
    for tracks in tracks_uri: #look through searched tracks uri
        selected_tracks_data = spotifyObject.audio_features(tracks) #get audio features of searched track
        for track_data in selected_tracks_data:
            if 0.8 <= track_data['energy'] <= 1.0:
                selectedWorkoutTracks_uri.append(track_data['uri'])
            elif 130 <= track_data['tempo'] <= 135:
                selectedWorkoutTracks_uri.append(track_data['uri'])
            elif 0.5 <= track_data['valence'] <= 1.0:
                selectedWorkoutTracks_uri.append(track_data['uri'])
            elif 0.7 <= track_data['loudness'] <= 1.0:
                selectedWorkoutTracks_uri.append(track_data['uri'])
        
    # for x in selectedWorkoutTracks_uri:
    #     print(x)
    return selectedWorkoutTracks_uri


def savePlaylist(spotifyObject, selectedWorkoutTracks_uri):
    # username = '1299050167'
    newPlaylist = spotifyObject.user_playlist_create(username, 'Spicify Workout')
    playlistId = newPlaylist['id'] #create id for new playlist
    spotifyObject.user_playlist_add_tracks(username, playlistId, selectedWorkoutTracks_uri, position=None)
   
workoutTracks_uri(spotifyObject, tracks_uri)
savePlaylist(spotifyObject, selectedWorkoutTracks_uri)

