import spotipy
import os
import spotipy.util as util
from json.decoder import JSONDecodeError
import json

username = "1299050167"
scope = 'user-library-read playlist-modify-public'

try:

    token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

except:

    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

spotifyObject = spotipy.Spotify(auth=token)

# Search query and results
searchResults2 = spotifyObject.search('genre:jazz+indie', 50, 0, 'track')
tracks = searchResults2['tracks']['items']

# print(tracks)
tracks_name = [] #empty list for track names
tracks_uri = [] #empty list for track uris
selectedStudyTracks_uri = [] # empty list to store songs for Study playlist
for x in tracks: #store searched songs in lists
#     tracks_name.append(x['name'])
#     if 70 <= x['popularity']:
    tracks_uri.append(x['uri'])

def studyPlaylist():
    for tracks in tracks_uri: #look through searched tracks uri
        selected_tracks_data = spotifyObject.audio_features(tracks) #get audio features of searched track
        for track_data in selected_tracks_data:
            if 0.0 <= track_data['energy'] <= 0.8:
                selectedStudyTracks_uri.append(track_data['uri'])
            elif 0.0 <= track_data['speechiness'] <= 1.0:
                selectedStudyTracks_uri.append(track_data['uri'])
            elif 0.0 <= track_data['loudness'] <= 1.0:
                selectedStudyTracks_uri.append(track_data['uri'])
    
    for x in selectedStudyTracks_uri:
        print(x)
    return selectedStudyTracks_uri

   
def savePlaylist():
    # username = '1299050167'
    newPlaylist = spotifyObject.user_playlist_create(username, 'Spicify Study 10/22/2019')
    playlistId = newPlaylist['id'] #create id for new playlist
    spotifyObject.user_playlist_add_tracks(username, playlistId, selectedStudyTracks_uri, position=None)

# studyPlaylist()
# savePlaylist(spotifyObject, selectedStudyTracks_uri)