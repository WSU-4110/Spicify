import pytest
import pytest_django
import spotipy

username = "22kpgi2vtrlebcei6eu37db7y"
scope = 'playlist-read-collaborative playlist-modify-private playlist-modify-public playlist-read-private user-modify-playback-state user-read-currently-playing user-read-playback-state user-read-private user-read-email user-library-modify user-library-read user-follow-modify user-follow-read user-read-recently-played user-top-read streaming app-remote-control'

try:

    token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

except:

    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

spotifyObject = spotipy.Spotify(auth=token)
user = spotifyObject.current_user()

# def test_workoutTracks_uri(self):
#     spotifyObject = spotipy.Spotify(auth=token)
#     user = spotifyObject.current_user()

#     searchResults = spotifyObject.search('genre:crunk+pop', 50, 0, 'track')
#     tracks = searchResults['tracks']['items']

#         for tracks in tracks_uri: #look through searched tracks uri
#             selected_tracks_data = spotifyObject.audio_features(tracks) #get audio features of searched track
#             for track_data in selected_tracks_data:
#                 if 0.7 <= track_data['energy'] <= 1.0:
#                     selectedWorkoutTracks_uri.append(track_data['uri'])
#                 elif 50 <= track_data['tempo'] <= 200:
#                     selectedWorkoutTracks_uri.append(track_data['uri'])
#                 elif 0.7 <= track_data['valence'] <= 1.0:
#                     selectedWorkoutTracks_uri.append(track_data['uri'])


#         return selectedWorkoutTracks_uri

# def test_savePlaylist(self):

#         for x in range(0,30):
#             randsongs.append(songs[random.randint(0,(len(songs) - 1))])     #Fill randsongs list with  30 randomly selected songs from playlist list
        
#         newPlaylist = spotifyObject.user_playlist_create(user['id'], 'Spicify Surprise Me')
#         playlistId = newPlaylist['id'] #create id for new playlist
#         spotifyObject.user_playlist_add_tracks(user['id'], playlistId, randsongs, position=None)

#         return playlistId

# def test_studyTracks_uri():
#     spotifyObject = spotipy.Spotify(auth=token)
#     user = spotifyObject.current_user()
#     selectedStudyTracks_uri = []

#     searchResults2 = spotifyObject.search('genre:jazz+indie', 50, 0, 'track')
#     tracks = searchResults2['tracks']['items']

#     for x in tracks: #store searched songs in lists
#         if 70 >= x['popularity']:
#                 tracks_uri.append(x['uri'])

#     for tracks in tracks_uri: #look through searched tracks uri
#         selected_tracks_data = spotifyObject.audio_features(tracks) #get audio features of searched track
#         for track_data in selected_tracks_data:
#             if 0.0 <= track_data['energy'] <= 0.8:
#                 selectedStudyTracks_uri.append(track_data['uri'])
#             elif 0.0 <= track_data['speechiness'] <= 1.0:
#                 selectedStudyTracks_uri.append(track_data['uri'])
#             elif 0.0 <= track_data['loudness'] <= 1.0:
#                 selectedStudyTracks_uri.append(track_data['uri'])

#     # for x in selectedStudyTracks_uri:
#     #     print(x)
#     assert selectedStudyTracks_uri


def test_internationalPlaylist(self):
        # setting up variables
        spotifyObject.user_playlist_create(user['id'], 'International Playlist')
        newPlaylist = spotifyObject.current_user_playlists()['items'][0]['id']
        newPlaylistUri = spotifyObject.current_user_playlists()['items'][0]['uri']

        songs = []
        randsongs = []

        # functionality
        searchResults = spotifyObject.search('Indian Chill', 1, 0, 'playlist')  # Indian Music

        playlistResult = searchResults['playlists']['items'][0]['id']
        playlistUser = searchResults['playlists']['items'][0]['owner']['display_name'] # Get playlists and playlist owners from search results

        playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

        for x in range(0,len(playlist['items'])):
            songs.append(playlist['items'][x]['track']['uri'])  #fill playlist list with all songs from search results

        searchResults = spotifyObject.search('Arab Mood Booster', 1, 0, 'playlist')       #Do another search for additional songs and veriety

        playlistResult = searchResults['playlists']['items'][0]['id']
        playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

        playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

        for x in range(0,len(playlist['items'])):
            songs.append(playlist['items'][x]['track']['uri'])  # add to playlist

        searchResults = spotifyObject.search('Arab Mood Booster', 1, 0, 'playlist')   # Arabic Music

        playlistResult = searchResults['playlists']['items'][0]['id']
        playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

        playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

        for x in range(0,len(playlist['items'])):
            songs.append(playlist['items'][x]['track']['uri'])  # add to playlist

            searchResults = spotifyObject.search('songs that get europeans turnt', 1, 0, 'playlist')   # European Music

        playlistResult = searchResults['playlists']['items'][0]['id']
        playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

        playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

        for x in range(0,len(playlist['items'])):
            songs.append(playlist['items'][x]['track']['uri'])  # add to playlist
        
        searchResults = spotifyObject.search('Korean Chill', 1, 0, 'playlist')       # Korean music

        playlistResult = searchResults['playlists']['items'][0]['id']
        playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

        playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

        for x in range(0,len(playlist['items'])):
            songs.append(playlist['items'][x]['track']['uri'])  # add to playlist

        searchResults = spotifyObject.search('African Heat', 1, 0, 'playlist')       # African music

        playlistResult = searchResults['playlists']['items'][0]['id']
        playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

        playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

        # for x in range(0,len(playlist['items'])):
        #     songs.append(playlist['items'][x]['track']['uri'])  # add to playlist

        for x in range(0,29):
            randsongs.append(songs[random.randint(0,(len(songs) - 1))])     #Fill randsongs list with  30 randomly selected songs from playlist list

        spotifyObject.user_playlist_add_tracks(user=userId, playlist_id=newPlaylist, tracks=randsongs)  #Fill playlist with songs from randsongs list

        Playlists = spotifyObject.current_user_playlists()['items'][0]['uri']
        playlistId = newPlaylist
        assert playlistId

def test_drivingTracks_uri(self):
        for tracks in tracks_uri: #look through searched tracks uri
            selected_tracks_data = spotifyObject.audio_features(tracks) #get audio features of searched track
            for track_data in selected_tracks_data:
                if 100 <= track_data['tempo'] <= 200:
                    selectedDrivingTracks_uri.append(track_data['uri'])
                elif 0.5 <= track_data['valence'] <= 1.0:
                    selectedDrivingTracks_uri.append(track_data['uri'])
                elif 0.4 <= track_data['liveness'] <= 1.0:
                    selectedDrivingTracks_uri.append(track_data['uri'])
        assert selectedDrivingTracks_uri    

def test_surpriseSearch(self):
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