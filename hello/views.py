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
            'picture': SpotipyFunctions.profile_pic,
            'playlist': playlistDisplay
        }
    )

def layout(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request, 
        'hello/layout.html',
        {
            'name': SpotipyFunctions.displayname,
            'picture': SpotipyFunctions.profile_pic,
            'playlist': playlistDisplay,
            'playlist': playlistDisplay
        }
    )

def workout(request):
    workoutObject = workoutPlaylistClass()
    workoutObject.workoutTracks_uri()
    passId = workoutObject.savePlaylist()
    url = workoutObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': SpotipyFunctions.profile_pic,
        }
    )

def study(request):
    studyObject = studyPlaylistClass()
    studyObject.studyTracks_uri()
    passId = studyObject.savePlaylist()
    url = studyObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': SpotipyFunctions.profile_pic,
        }
    )

def driving(request):
    drivingObject = drivingPlaylistClass()
    drivingObject.drivingTracks_uri()
    passId = drivingObject.savePlaylist()
    url = drivingObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': SpotipyFunctions.profile_pic,
        }
    )


def yearRange(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/yearRangeChoices.html',
        {
            'playlistName': YearRangePlaylist.playlist_name,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': SpotipyFunctions.profile_pic,
        }
    )

def thirties(request):
    yearObject = yearRangePlaylistClass()
    passId = yearObject.thirtiesPlaylist()
    url = yearObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': SpotipyFunctions.profile_pic,
        }
    )

def fourties(request):
    yearObject = yearRangePlaylistClass()
    passId = yearObject.fourtiesPlaylist()
    url = yearObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': SpotipyFunctions.profile_pic,
        }
    )

def fifties(request):
    yearObject = yearRangePlaylistClass()
    passId = yearObject.fiftiesPlaylist()
    url = yearObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': SpotipyFunctions.profile_pic,
        }
    )

def sixties(request):
    yearObject = yearRangePlaylistClass()
    passId = yearObject.sixtiesPlaylist()
    url = yearObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': SpotipyFunctions.profile_pic,
        }
    )

def seventies(request):
    yearObject = yearRangePlaylistClass()
    passId = yearObject.SeventiesPlaylist()
    url = yearObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': SpotipyFunctions.profile_pic,
        }
    )

def eighties(request):
    yearObject = yearRangePlaylistClass()
    passId = yearObject.eightiesPlaylist()
    url = yearObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': SpotipyFunctions.profile_pic,
        }
    )

def nineties(request):
    yearObject = yearRangePlaylistClass()
    passId = yearObject.NinetiesPlaylist()
    url = yearObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': SpotipyFunctions.profile_pic,
        }
    )

def millenial(request):
    yearObject = yearRangePlaylistClass()
    passId = yearObject.millennialPlaylist()
    url = yearObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': SpotipyFunctions.profile_pic,
        }
    )

def international(request):
    intObject = internationalPlaylistClass()
    passId = intObject.internationalPlaylist()
    url = intObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': SpotipyFunctions.profile_pic,
        }
    )

def artists(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/artists.html',
        {
            'name': SpotipyFunctions.displayname,
            'picture': SpotipyFunctions.profile_pic,
            'playlist': playlistDisplay
        }
    )

def uncleposty(request):
    raObj = relatedArtistsPlaylistClass()
    raObj.unclepostyPlaylist()
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'picture': SpotipyFunctions.profile_pic,
            'playlist': playlistDisplay
        }
    )

def selenagomez(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'picture': SpotipyFunctions.profile_pic,
            'playlist': playlistDisplay
        }
    )

def rezz(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'picture': SpotipyFunctions.profile_pic,
            'playlist': playlistDisplay
        }
    )

def atribecalledquest(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'picture': SpotipyFunctions.profile_pic,
            'playlist': playlistDisplay
        }
    )

def travisscott(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'picture': SpotipyFunctions.profile_pic,
            'playlist': playlistDisplay
        }
    )

def timmcgraw(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'picture': SpotipyFunctions.profile_pic,
            'playlist': playlistDisplay
        }
    )

def nancyajram(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'picture': SpotipyFunctions.profile_pic,
            'playlist': playlistDisplay
        }
    )

def prince(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'picture': SpotipyFunctions.profile_pic,
            'playlist': playlistDisplay
        }
    )
def rate(request):
    rating = request.GET['rate']
    SpotipyFunctions.ratePlaylists(rating)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/category.html',
        {
            'name': SpotipyFunctions.displayname,
            'picture': SpotipyFunctions.profile_pic,
            'playlist': playlistDisplay
        }
    )
