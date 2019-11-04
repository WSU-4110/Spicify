from django.http import HttpResponse
from django.shortcuts import render
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
    
 
