from django.http import HttpResponse
from django.shortcuts import render
from hello import YearRangePlaylist
from hello import SpotipyFunctions
from hello import WorkoutPlaylist
from hello import StudyPlaylist
from hello import GeneralDrivingPlaylist
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
            'playlistName': WorkoutPlaylist.playlist_name,
            'name': SpotipyFunctions.displayname
        }
    )

def study(request):
    StudyPlaylist.studyPlaylist()
    StudyPlaylist.savePlaylist()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistName': StudyPlaylist.playlist_name,
            'name': SpotipyFunctions.displayname
        }
    )

def driving(request):
    GeneralDrivingPlaylist.drivingTracks_uri()
    GeneralDrivingPlaylist.savePlaylist()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistName': GeneralDrivingPlaylist.playlist_name,
            'name': SpotipyFunctions.displayname
        }
    )
    

def yearRange(request):
    return render(
        request,
        'hello/yearRangeChoices.html',
        {
            'playlistName': YearRangePlaylist.playlist_name,
            'name': SpotipyFunctions.displayname
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
