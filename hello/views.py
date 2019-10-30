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
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': SpotipyFunctions.displayname,
            'followers': SpotipyFunctions.followers
        }
    )

def category(request):
    return render(request, 'hello/category.html')

def layout(request):
    return render(request, 'hello/layout.html')

def workout(request):
    WorkoutPlaylist.workoutTracks_uri()
    WorkoutPlaylist.savePlaylist()
    return render(request, 'hello/home.html')

def study(request):
    StudyPlaylist.studyPlaylist()
    StudyPlaylist.savePlaylist()
    return render(request, 'hello/home.html')

def driving(request):
    GeneralDrivingPlaylist.drivingTracks_uri()
    GeneralDrivingPlaylist.savePlaylist()
    return render(request, 'hello/home.html')
    
 