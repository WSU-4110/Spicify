from django.http import HttpResponse
from django.shortcuts import render
from hello import YearRangePlaylist
from hello import SpotipyFunctions
from hello.WorkoutPlaylist import *
from hello import GeneralDrivingPlaylist
from hello import InternationalPlaylist
from hello.StudyPlaylist import studyPlaylistClass
import requests

def home(request):
    return render(request, 'hello/home.html')

def hello_there(request, name):
    return render(request,'hello/hello_there.html')

def category(request):
    return render(
        request,
        'hello/category.html',
        {
            'name': SpotipyFunctions.displayname,
            'followers': SpotipyFunctions.followers
        }
    )

def layout(request):
    return render(request, 'hello/layout.html')

def workout(request):
    FactoryObj = PlaylistFactory()
    playlist1 = FactoryObj.CreatePlaylist("workout")
    playlist1.generateURIs()
    playlistId = playlist1.savePlaylist()
    playlistUrl = playlist1.showPlaylist(playlistId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': 'Spicify Workout',
            'playlistUrl': playlistUrl
        }
    )

def study(request):
    studyObject = studyPlaylistClass()
    studyObject.studyPlaylist()
    passId = studyObject.savePlaylist()
    url = studyObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': 'Spicify Study',
            'playlistUrl': url
        }
    )

def driving(request):
    GeneralDrivingPlaylist.drivingTracks_uri()
    GeneralDrivingPlaylist.savePlaylist()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': GeneralDrivingPlaylist.playlist_name
        }
    )
    

def yearRange(request):
    return render(
        request,
        'hello/yearRangeChoices.html',
        {
            'name': YearRangePlaylist.playlist_name
        }
    )

def thirties(request):
    YearRangePlaylist.thirtiesPlaylist()
    return render(
        request,
        'hello/playlist_view.html'
    )

def fourties(request):
    YearRangePlaylist.fourtiesPlaylist()
    return render(
        request,
        'hello/playlist_view.html'
    )

def fifties(request):
    YearRangePlaylist.fiftiesPlaylist()
    return render(
        request,
        'hello/playlist_view.html'
    )

def sixties(request):
    YearRangePlaylist.sixtiesPlaylist()
    return render(
        request,
        'hello/playlist_view.html'
    )

def seventies(request):
    YearRangePlaylist.SeventiesPlaylist()
    return render(
        request,
        'hello/playlist_view.html'
    )

def eighties(request):
    YearRangePlaylist.eightiesPlaylist()
    return render(
        request,
        'hello/playlist_view.html'
    )

def nineties(request):
    YearRangePlaylist.NinetiesPlaylist()
    
    return render(
        request,
        'hello/playlist_view.html'
    )

def millenial(request):
    YearRangePlaylist.millennialPlaylist()
    return render(
        request,
        'hello/playlist_view.html'
    )

def international(request):
    InternationalPlaylist.internationalPlaylist()
    return render(
        request,
        'hello/playlist_view.html'
    )