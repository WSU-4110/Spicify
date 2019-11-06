from django.http import HttpResponse
from django.shortcuts import render
from hello import YearRangePlaylist
from hello import SpotipyFunctions
from hello import WorkoutPlaylist
from hello import StudyPlaylist
from hello import GeneralDrivingPlaylist
from hello import InternationalPlaylist
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
    WorkoutPlaylist.workoutTracks_uri()
    WorkoutPlaylist.savePlaylist()
    return render(
        request, 
        'hello/playlist_view.html',
        {
            'name': WorkoutPlaylist.playlist_name
        }
    )

def study(request):
    StudyPlaylist.studyPlaylist()
    StudyPlaylist.savePlaylist()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': StudyPlaylist.playlist_name
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