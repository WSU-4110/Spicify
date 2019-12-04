# from hello import YearRangePlaylist
import spotipy
import pytest
songs = []

username = '22kpgi2vtrlebcei6eu37db7y'
scope = 'playlist-read-collaborative playlist-modify-private playlist-modify-public playlist-read-private user-modify-playback-state user-read-currently-playing user-read-playback-state user-read-private user-read-email user-library-modify user-library-read user-follow-modify user-follow-read user-read-recently-played user-top-read streaming app-remote-control'
token = 'BQA4VLI_ncjWGLrubp711AZy3ID5sVEurbo5Wk4iDkEIO0t8fnc9Oi2IxTshx9prSO_bdTDXzvl_wZ3wi6fccq0STs1Vt_YCaGVP9_f83RECHZkDWn31V310c5oSN-OvunaVyGm6kxGifa7tfVMcedeNzvPLTcLIydUWDPSm4rgB6p9vrl4rTFtoy_KInQhfOXXD-K9PLXbuvrpYzYG1zqeqj538MijD6Hp1hGh8pCNlRVoiaRumzped8gW53w9NHNwglU6-4ZG31ceT8y89-A", "token_type": "Bearer", "expires_in": 3600, "refresh_token": "AQCZx3JTYNMVDmXDZVYhWILm2tVYfWQNn9Hx7L7tT20o0hgYyzpdrn3rfYSX3xMpSXcmnQfD2Rm4_R5VMIhsesb7Ze3CH3RXixCQHX2USsK67OlDyblu2L5g6b7VeIcAtZ8'
# token will expire must be renewed before test is run to refresh token delete the cache and run the project again, the new token with be in the new cache

def test_unclepostyPlaylist():
    spotifyObject = spotipy.Spotify(auth=token)     # create object of type spotipy
    user = spotifyObject.current_user()             # get current app user
    
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
    spotifyObject = spotipy.Spotify(auth=token)     # create object of type spotipy
    user = spotifyObject.current_user()             # get current app user
    
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
    spotifyObject = spotipy.Spotify(auth=token)     # create object of type spotipy
    user = spotifyObject.current_user()             # get current app user
    
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
    spotifyObject = spotipy.Spotify(auth=token)     # create object of type spotipy
    user = spotifyObject.current_user()             # get current app user
    
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
    spotifyObject = spotipy.Spotify(auth=token)     # create object of type spotipy
    user = spotifyObject.current_user()             # get current app user
    
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
    spotifyObject = spotipy.Spotify(auth=token)     # create object of type spotipy
    user = spotifyObject.current_user()             # get current app user
    
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



