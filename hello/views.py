
# import re
# from datetime import datetime

# # Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
# import os
# import sys
# import json
# import spotipy
# import webbrowser
# import spotipy.util as util
# from json.decoder import JSONDecodeError
# import spotipy.client
# import spotipy.oauth2
# import spotipy.util

def home(request):
     return render(request, "hello/home.html")

     # username = input("Spotify Username: ")
     # scope = 'user-read-private user-read-playback-state user-modify-playback-state'

     # try:

     #      token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

     # except:

     #      os.remove(f".cache-{username}")
     #      token = util.prompt_for_user_token(username,scope,client_id='8ff0ccc6f1fb460e8fabbe33e0e42112',client_secret='03d0e4de0957434abcc60660045d7cfc',redirect_uri='https://www.google.com/')

     # spotifyObject = spotipy.Spotify(auth=token)


     # user = spotifyObject.current_user()
     # displayname = user['display_name']
     # followers = user['followers']['total']


     # print()
     # print("Welcome to Spicify " + displayname, "!")
     # print("You have " + str(followers) + " followers.")
    


def category(request):
     return render(request, "hello/category.html")

# def about(request):
#     return render(request, "hello/about.html")

# def hello_there(request, name):
#     return render(
#         request,
#         'hello/hello_there.html',
#         {
#             'name': name,
#             'date': datetime.now()
#         }
#     )



