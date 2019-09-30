import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
import spotipy.client
import spotipy.oauth2
import spotipy.util

username = input("Enter Your Username: ")
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

# 22kpgi2vtrlebcei6eu37db7y

try:

    token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

except:

    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

spotifyObject = spotipy.Spotify(auth=token)

#Get Current Device

devices = spotifyObject.devices()
print(json.dumps(devices, sort_keys=True, indent=4))
deviceID = devices['devices'][0]['id']

#Current track information

track = spotifyObject.current_user_playing_track()
print(json.dumps(track, sort_keys=True, indent=4))
print()
artist = track['item']['artists'][0]['name']
track = track['item']['name']

if artist == "":
    print("Not Currently Play a Song")

if artist != "":
    print("Currently playing " + track)

user = spotifyObject.current_user()

displayname = user['display_name']
followers = user['followers']['total']

while True:

    print()
    print("Welcome to Spicify " + displayname, "!")
    print("You have " + str(followers) + " followers.")
    print()
    print("0 - Search for artist")
    print("1 - exit")
    print()
    choice = input("Your choice: ")

    # Search for the artist
    if choice == "0":
        print("0")
        searchQuery = input("ok, what's their name?: ")
        print()

        # Get Search results
        searchResults = spotifyObject.search(searchQuery,1,0,"artist")

        artist = searchResults['artists']['items'][0]
        print(artist['name'])
        print(str(artist['followers']['total']) + " followers")
        print(artist['genres'][0])
        print()
        webbrowser.open(artist['images'][0]['url'])
        artistID = artist['id']

        # Album and track details
        trackURIs = []
        trackArt = []
        z = 0

        # Extract album data

        albumResults = spotifyObject.artist_albums(artistID)
        albumResults = albumResults['items']

        for item in albumResults:
            print("Album " + item['name'])
            albumID = item['id']
            albumArt = item['images'][0]['url']

            # Extract track data
            trackResults = spotifyObject.album_tracks(albumID)
            trackResults = trackResults['items']

            for item in trackResults:
                print(str(z) + ": " + item['name'])
                trackURIs.append(item['uri'])
                trackArt.append(albumArt)
                z+=1
            print()

        # See album art
        while True:
            songSelection = input("Enter a song number to see the album art associated with it and play the song (x to exit): " )
            if songSelection == "x":
                break
            trackSelectionList = []
            trackSelectionList.append(trackURIs[int(songSelection)])
            spotifyObject.start_playback(deviceID, None, trackSelectionList)
            webbrowser.open(trackArt[int(songSelection)])

    if choice == "1":
        break    

# Python Classes.py 22kpgi2vtrlebcei6eu37db7y

# print(json.dumps(VARIABLE, sort_keys=True, indent=4))