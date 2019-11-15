from django.http import HttpResponse
from django.shortcuts import render
from hello import YearRangePlaylist
from hello.YearRangePlaylist import yearRangePlaylistClass
from hello import SpotipyFunctions
from hello.WorkoutPlaylist import workoutPlaylistClass
from hello.GeneralDrivingPlaylist import drivingPlaylistClass
from hello.InternationalPlaylist import internationalPlaylistClass
from hello.StudyPlaylist import studyPlaylistClass
from hello.RelatedArtistsPlaylist import relatedArtistsPlaylistClass
import requests

def home(request):
    return render(request, 'hello/home.html')

def hello_there(request, name):
    return render(request,'hello/hello_there.html')

def category(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    print(playlistDisplay)
    return render(
        request,
        'hello/category.html',
        {
            'name': SpotipyFunctions.displayname,
            'followers': SpotipyFunctions.followers,
            'playlist': playlistDisplay
        }
    )

def layout(request):
    return render(request, 'hello/layout.html')

def workout(request):
    workoutObject = workoutPlaylistClass()
    workoutObject.workoutTracks_uri()
    passId = workoutObject.savePlaylist()
    url = workoutObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url
        }
    )

def study(request):
    studyObject = studyPlaylistClass()
    studyObject.studyTracks_uri()
    passId = studyObject.savePlaylist()
    url = studyObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url
        }
    )

def driving(request):
    drivingObject = drivingPlaylistClass()
    drivingObject.drivingTracks_uri()
    passId = drivingObject.savePlaylist()
    url = drivingObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url
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
    yearObject = yearRangePlaylistClass()
    passId = yearObject.thirtiesPlaylist()
    url = yearObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url
        }
    )

def fourties(request):
    yearObject = yearRangePlaylistClass()
    passId = yearObject.fourtiesPlaylist()
    url = yearObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url
        }
    )

def fifties(request):
    yearObject = yearRangePlaylistClass()
    passId = yearObject.fiftiesPlaylist()
    url = yearObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url
        }
    )

def sixties(request):
    yearObject = yearRangePlaylistClass()
    passId = yearObject.sixtiesPlaylist()
    url = yearObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url
        }
    )

def seventies(request):
    yearObject = yearRangePlaylistClass()
    passId = yearObject.SeventiesPlaylist()
    url = yearObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url
        }
    )

def eighties(request):
    yearObject = yearRangePlaylistClass()
    passId = yearObject.eightiesPlaylist()
    url = yearObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url
        }
    )

def nineties(request):
    yearObject = yearRangePlaylistClass()
    passId = yearObject.NinetiesPlaylist()
    url = yearObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url
        }
    )

def millenial(request):
    yearObject = yearRangePlaylistClass()
    passId = yearObject.millennialPlaylist()
    url = yearObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url
        }
    )

def international(request):
    intObject = internationalPlaylistClass()
    passId = intObject.internationalPlaylist()
    url = intObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url
        }
    )

def artists(request):
    return render(
        request,
        'hello/artists.html'
    )

def uncleposty(request):
    raObj = relatedArtistsPlaylistClass()
    raObj.unclepostyPlaylist()
    return render(
        request,
        'hello/playlist_view.html'
    )

def selenagomez(request):
    return render(
        request,
        'hello/playlist_view.html'
    )

def rezz(request):
    return render(
        request,
        'hello/playlist_view.html'
    )

def atribecalledquest(request):
    return render(
        request,
        'hello/playlist_view.html'
    )

def travisscott(request):
    return render(
        request,
        'hello/playlist_view.html'
    )

def timmcgraw(request):
    return render(
        request,
        'hello/playlist_view.html'
    )

def nancyajram(request):
    return render(
        request,
        'hello/playlist_view.html'
    )

def prince(request):
    return render(
        request,
        'hello/playlist_view.html'
    )
