# from hello import YearRangePlaylist
import spotipy
import pytest
songs = []

username = '22kpgi2vtrlebcei6eu37db7y'
scope = 'playlist-read-collaborative playlist-modify-private playlist-modify-public playlist-read-private user-modify-playback-state user-read-currently-playing user-read-playback-state user-read-private user-read-email user-library-modify user-library-read user-follow-modify user-follow-read user-read-recently-played user-top-read streaming app-remote-control'
token = 'BQBV0Kfdhy9C4lAHEIY40l6se4HdeUz9fUCpC1XGhw1T-3AeZXYO5uAUGgQwjcWT6RVW6Lvb3SUuQmPy9WU0AdPPVkamoXpyHf8bFBECGFTJotag-ZAbHM0tXfgau5Amz7XLpeHiqKXPR-2_UjSRy8_ND0KXGehWiOMLiMTZ-n8ZKH5sqmjscpQDLMfkWlqI0e6AU3UHrEWCzWpVCNAS0tUpsUN2hAxK0Eg6CoYffheJ2xX_fpUIPgYmZnU1f7hC03ZyYa6_J6UJArDIcHcGPw", "token_type": "Bearer", "expires_in": 3600, "refresh_token": "AQDFL3kgini8AUy8UDEtAtXzi82qB11ZhkJHICwjFKvfig9hBlHjcIF_idoxnEQX9JeqSrg2NUZ6weeVwKhXJpJMd_B9rINfM23zT-HHdj2ZZ_SYTvpM2pFKwQdtP8Uosxo'
# token will expire must be renewed before test is run to refresh token uncomment line 2 of test_pytest.py

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



