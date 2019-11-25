import pytest
# from hello.RelatedArtistsPlaylist import relatedArtistsPlaylistClass   # code to test
import spotipy
songs = []

username = '22kpgi2vtrlebcei6eu37db7y'
scope = 'playlist-read-collaborative playlist-modify-private playlist-modify-public playlist-read-private user-modify-playback-state user-read-currently-playing user-read-playback-state user-read-private user-read-email user-library-modify user-library-read user-follow-modify user-follow-read user-read-recently-played user-top-read streaming app-remote-control'
token = 'BQDxHJrwhgxHwJX6V26sXs88dAHN_spqWmvKmnPMFarJBElwJQIet8hixNCUFrikyG5pidN8iCNSAab8J3np2LQGuEOfykY6LMh5QWb9KraVfQpdHFofAk0A57Tko2aAgcQFrG7Au2QPc36vTm6fP-pI-7Zj30gYsuXVYMgi2iPHlc3gnOytcc-mm7kfg5os7plj9gAN_5ZkhXgxJ82JL-Bgf8qvnGTL9mA2eRY9aO_DzCUtm8ZoI2tH9c3y0uMF70fg1TAQjKUeIqZxM0upEw", "token_type": "Bearer", "expires_in": 3600, "refresh_token": "AQBLgn1t6OtypM2XZUyAhAQFL2MA0RBUePj1XhxyiRJdwzEmZnevxegV0SxnVwH1ug98zG1bMZ81y_cP7BV9bdzJjQT26733itBVb3l1HaCTVbAhDS0WZ4CjXXPbIDrZIa0'
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
