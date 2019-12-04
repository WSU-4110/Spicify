import spotipy
import pytest
import random
songs = []

username = '22kpgi2vtrlebcei6eu37db7y'
scope = 'playlist-read-collaborative playlist-modify-private playlist-modify-public playlist-read-private user-modify-playback-state user-read-currently-playing user-read-playback-state user-read-private user-read-email user-library-modify user-library-read user-follow-modify user-follow-read user-read-recently-played user-top-read streaming app-remote-control'
token = 'BQCN_Qj1OqAJsWq_TO0GKJdsMixcT37Gr0tMpR2cAYYMNq0Y0ah4PCA74BsEBkERecofdJ9oHcXpOnmHezdaEqmgiJtwwBiqgnkQm7qJ__rn5iqkc8vrkoeNg2GkYZaM_OJ86ROKQDcXMJXrSmpHDZvah5WK7R3ORrAQQMRvXfR8vXEUL4pZkD3GTMEVhUsDe_gkh6RgPst7NhdXyEpLvS_AuecxjpUqZuW2i5_hhQ1qBzsUfE2HbEF4wkQQosKizuPjuXLqzLdogQDhwX7pvw'
# token will expire must be renewed before test is run to refresh token delete the cache and run the project again, the new token with be in the new cache

def test_unclepostyPlaylist():
    spotifyObject = spotipy.Spotify(auth=token)     # create object of type spotipy - testing purposes
    user = spotifyObject.current_user()             # get current app user - testing purposes
    
    searchResults = spotifyObject.search('Post+Malone', 1, 0, 'artist')     # search for selected artist object
    getArtist = searchResults['artists']['items'][0]
    artistId = getArtist['id']          # get slected artist's Id

    relatedArtists = spotifyObject.artist_related_artists(artistId)
    artists = relatedArtists['artists']     # search for related artists

    for x in artists:
        artistName = (x['name'])
        artistSearch = spotifyObject.search(artistName, 2, 0 ,'track')      # search all related artists and get tracks
        tracks = artistSearch['tracks']['items']
        for x in tracks:
            songs.append(x['uri']) 

    #test if name returned matches selected artist's name
    assert searchResults['artists']['items'][0]['name'] == 'Post Malone'

    #test if related artists list comes back null
    assert relatedArtists != [] 

    #test if related artists tracks search come back null
    assert tracks != []

def test_selenagomezPlaylist():
    spotifyObject = spotipy.Spotify(auth=token)     # create object of type spotipy - testing purposes
    user = spotifyObject.current_user()             # get current app user - testing purposes
    
    searchResults = spotifyObject.search('Selena+Gomez', 1, 0, 'artist')     # search for selected artist object
    getArtist = searchResults['artists']['items'][0]
    artistId = getArtist['id']          # get slected artist's Id

    relatedArtists = spotifyObject.artist_related_artists(artistId)
    artists = relatedArtists['artists']     # search for related artists

    for x in artists:
        artistName = (x['name'])
        artistSearch = spotifyObject.search(artistName, 2, 0 ,'track')      # search all related artists and get tracks
        tracks = artistSearch['tracks']['items']
        for x in tracks:
            songs.append(x['uri']) 

    #test if name returned matches selected artist's name
    assert searchResults['artists']['items'][0]['name'] == 'Selena Gomez'

    #test if related artists list comes back null
    assert relatedArtists != [] 

    #test if related artists tracks search come back null
    assert tracks != []


def test_rezzPlaylist():
    spotifyObject = spotipy.Spotify(auth=token)     # create object of type spotipy - testing purposes
    user = spotifyObject.current_user()             # get current app user - testing purposes
    
    searchResults = spotifyObject.search('Rezz', 1, 0, 'artist')     # search for selected artist object
    getArtist = searchResults['artists']['items'][0]
    artistId = getArtist['id']          # get slected artist's Id

    relatedArtists = spotifyObject.artist_related_artists(artistId)
    artists = relatedArtists['artists']     # search for related artists

    for x in artists:
        artistName = (x['name'])
        artistSearch = spotifyObject.search(artistName, 2, 0 ,'track')      # search all related artists and get tracks
        tracks = artistSearch['tracks']['items']
        for x in tracks:
            songs.append(x['uri']) 

    #test if name returned matches selected artist's name
    assert searchResults['artists']['items'][0]['name'] == 'Rezz'

    #test if related artists list comes back null
    assert relatedArtists != [] 

    #test if related artists tracks search come back null
    assert tracks != []


def test_atribecalledquestPlaylist():
    spotifyObject = spotipy.Spotify(auth=token)     # create object of type spotipy - testing purposes
    user = spotifyObject.current_user()             # get current app user - testing purposes
    
    searchResults = spotifyObject.search('A+Tribe+Called+Quest', 1, 0, 'artist')     # search for selected artist object
    getArtist = searchResults['artists']['items'][0]
    artistId = getArtist['id']          # get slected artist's Id

    relatedArtists = spotifyObject.artist_related_artists(artistId)
    artists = relatedArtists['artists']     # search for related artists

    for x in artists:
        artistName = (x['name'])
        artistSearch = spotifyObject.search(artistName, 2, 0 ,'track')      # search all related artists and get tracks
        tracks = artistSearch['tracks']['items']
        for x in tracks:
            songs.append(x['uri']) 

    #test if name returned matches selected artist's name
    assert searchResults['artists']['items'][0]['name'] == 'A Tribe Called Quest'

    #test if related artists list comes back null
    assert relatedArtists != [] 

    #test if related artists tracks search come back null
    assert tracks != []

def test_travisscottPlaylist():
    spotifyObject = spotipy.Spotify(auth=token)     # create object of type spotipy - testing purposes
    user = spotifyObject.current_user()             # get current app user - testing purposes
    
    searchResults = spotifyObject.search('Travis+Scott', 1, 0, 'artist')     # search for selected artist object
    getArtist = searchResults['artists']['items'][0]
    artistId = getArtist['id']          # get slected artist's Id

    relatedArtists = spotifyObject.artist_related_artists(artistId)
    artists = relatedArtists['artists']     # search for related artists

    for x in artists:
        artistName = (x['name'])
        artistSearch = spotifyObject.search(artistName, 2, 0 ,'track')      # search all related artists and get tracks
        tracks = artistSearch['tracks']['items']
        for x in tracks:
            songs.append(x['uri']) 

    #test if name returned matches selected artist's name
    assert searchResults['artists']['items'][0]['name'] == 'Travis Scott'

    #test if related artists list comes back null
    assert relatedArtists != [] 

    #test if related artists tracks search come back null
    assert tracks != []

def test_timmcgrawPlaylist():
    spotifyObject = spotipy.Spotify(auth=token)     # create object of type spotipy - testing purposes
    user = spotifyObject.current_user()             # get current app user - testing purposes
    
    searchResults = spotifyObject.search('Tim+McGraw', 1, 0, 'artist')     # search for selected artist object
    getArtist = searchResults['artists']['items'][0]
    artistId = getArtist['id']          # get slected artist's Id

    relatedArtists = spotifyObject.artist_related_artists(artistId)
    artists = relatedArtists['artists']     # search for related artists

    for x in artists:
        artistName = (x['name'])
        artistSearch = spotifyObject.search(artistName, 2, 0 ,'track')      # search all related artists and get tracks
        tracks = artistSearch['tracks']['items']
        for x in tracks:
            songs.append(x['uri']) 

    #test if name returned matches selected artist's name
    assert searchResults['artists']['items'][0]['name'] == 'Tim McGraw'

    #test if related artists list comes back null
    assert relatedArtists != [] 

    #test if related artists tracks search come back null
    assert tracks != []



def test_30sPlaylist():
    spotifyObject = spotipy.Spotify(auth=token)     # create object of type spotipy - testing purposes
    user = spotifyObject.current_user()             # get current app user - testing purposes
    userId = user['id']                             # get user Id - testing purposes
    spotifyObject.user_playlist_create(user['id'], '1930s Playlist')
    newPlaylist = spotifyObject.current_user_playlists()['items'][0]['id']          #Create new empty playlist
    newPlaylistUri = spotifyObject.current_user_playlists()['items'][0]['uri']

    songs = []
    randsongs = []      #Empty Arrays to store songs

    searchResults = spotifyObject.search('1930s jazz', 1, 0, 'playlist')   #search for music

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']  #Get playlists and playlist owners from search results

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])  #fill playlist list with all songs from search results

    searchResults = spotifyObject.search('1930s music', 1, 0, 'playlist')   #search for music

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']  #Get playlists and playlist owners from search results

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])  #fill playlist list with all songs from search results

    searchResults = spotifyObject.search('1930', 1, 0, 'playlist')   #search for music

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']  #Get playlists and playlist owners from search results

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])  #fill playlist list with all songs from search results

    searchResults = spotifyObject.search('1930s swing', 1, 0, 'playlist')       #Do another search for additional songs and veriety

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])  #Add more songs to playlist list


    for x in range(0,30):
        randsongs.append(songs[random.randint(0,(len(songs) - 1))])     #Fill randsongs list with  30 randomly selected songs from playlist list


    spotifyObject.user_playlist_add_tracks(user=userId, playlist_id=newPlaylist, tracks=randsongs)  #Fill playlist with songs from randsongs list

    Playlists = spotifyObject.current_user_playlists()['items'][0]['uri']
    playlistId = newPlaylist
    return playlistId

    assert YearRangePlaylist.yearRangePlaylistClass().thirtiesPlaylist() == 30


def test_40sPlaylist():
    spotifyObject = spotipy.Spotify(auth=token)     # create object of type spotipy - testing purposes
    user = spotifyObject.current_user()             # get current app user - testing purposes
    userId = user['id']                             # get user Id - testing purposes
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

    searchResults = spotifyObject.search('1940s big bands', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])


    for x in range(0,29):
        randsongs.append(songs[random.randint(0,(len(songs) - 1))])

    print(randsongs)

    spotifyObject.user_playlist_add_tracks(user=userId, playlist_id=newPlaylist, tracks=randsongs)

    Playlists = spotifyObject.current_user_playlists()['items'][0]['uri']
    playlistId = newPlaylist
    return playlistId
        
    assert YearRangePlaylist.yearRangePlaylistClass().fourtiesPlaylist() == 30


def test_50sPlaylist():
    spotifyObject = spotipy.Spotify(auth=token)     # create object of type spotipy - testing purposes
    user = spotifyObject.current_user()             # get current app user - testing purposes
    userId = user['id']                             # get user Id - testing purposes

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

    searchResults = spotifyObject.search('1950s rock and roll', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])

    searchResults = spotifyObject.search('1950s love songs', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])

    searchResults = spotifyObject.search('1950s jazz', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])

    for x in range(0,29):
        randsongs.append(songs[random.randint(0,(len(songs) - 1))])

    spotifyObject.user_playlist_add_tracks(user=userId, playlist_id=newPlaylist, tracks=randsongs)

    Playlists = spotifyObject.current_user_playlists()['items'][0]['uri']
    playlistId = newPlaylist
    return playlistId

    assert YearRangePlaylist.yearRangePlaylistClass().fiftiesPlaylist() == 30

def test_60sPlaylist():
    spotifyObject = spotipy.Spotify(auth=token)     # create object of type spotipy - testing purposes
    user = spotifyObject.current_user()             # get current app user - testing purposes
    userId = user['id']                             # get user Id - testing purposes

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

    searchResults = spotifyObject.search('1960s soul', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])

    searchResults = spotifyObject.search('1960 something', 1, 0, 'playlist')

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

    Playlists = spotifyObject.current_user_playlists()['items'][0]['uri']
    playlistId = newPlaylist
    return playlistId

    assert YearRangePlaylist.yearRangePlaylistClass().sixtiesPlaylist() == 30

def test_80sPlaylist():
    spotifyObject = spotipy.Spotify(auth=token)     # create object of type spotipy - testing purposes
    user = spotifyObject.current_user()             # get current app user - testing purposes
    userId = user['id']                             # get user Id - testing purposes

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

    searchResults = spotifyObject.search('1980s love songs', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])

    searchResults = spotifyObject.search('1980s rock', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])


    searchResults = spotifyObject.search('1980s retrogamer', 1, 0, 'playlist')

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

    Playlists = spotifyObject.current_user_playlists()['items'][0]['uri']
    playlistId = newPlaylist
    return playlistId

    assert YearRangePlaylist.yearRangePlaylistClass().eightiesPlaylist() == 30
    
def test_70sPlaylist():
    spotifyObject = spotipy.Spotify(auth=token)     # create object of type spotipy - testing purposes
    user = spotifyObject.current_user()             # get current app user - testing purposes
    userId = user['id']                             # get user Id - testing purposes

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

    searchResults = spotifyObject.search('All out 70s', 1, 0, 'playlist')

    playlistResult = searchResults['playlists']['items'][0]['id']
    playlistUser = searchResults['playlists']['items'][0]['owner']['display_name']

    playlist = spotifyObject.user_playlist_tracks(user=playlistUser,playlist_id=playlistResult)

    for x in range(0,len(playlist['items'])):
        songs.append(playlist['items'][x]['track']['uri'])

    searchResults = spotifyObject.search('1970s love songs', 1, 0, 'playlist')

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

    Playlists = spotifyObject.current_user_playlists()['items'][0]['uri']
    playlistId = newPlaylist
    return playlistId
        
    assert YearRangePlaylist.yearRangePlaylistClass().SeventiesPlaylist() == 30

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
        selected_tracks_data = spotifyObject.audio_features(tracks)  # get audio features of searched track
        for track_data in selected_tracks_data:
            if 0.7 <= track_data['energy'] <= 1.0:
                selectedWorkoutTracks_uri.append(track_data['uri'])
            elif 50 <= track_data['tempo'] <= 200:
                selectedWorkoutTracks_uri.append(track_data['uri'])
            elif 0.7 <= track_data['valence'] <= 1.0:
                selectedWorkoutTracks_uri.append(track_data['uri'])
        assert len(selectedWorkoutTracks_uri) != 0

    
def test_savePlaylist():
    spotifyObject = spotipy.Spotify(auth=token)
    user = spotifyObject.current_user()
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
    spotifyObject = spotipy.Spotify(auth=token)
    # Search query and results
    searchResults3 = spotifyObject.search('genre:rock', 50, 0, 'track')
    tracks = searchResults3['tracks']['items']

    for x in tracks:  # store searched songs in lists
        songs.append(x['uri'])

    assert len(songs) > 2


def test_internationalPlaylist():
    # setting up variables
    
    spotifyObject = spotipy.Spotify(auth=token)
    user = spotifyObject.current_user()
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

    spotifyObject = spotipy.Spotify(auth=token)

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