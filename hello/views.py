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
from hello.SurpriseMePlaylist import surprisePlaylistClass
import requests

def home(request):
    return render(request, 'hello/home.html')

def hello_there(request, name):
    return render(request,'hello/hello_there.html')

def category(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    # print(playlistDisplay)
    return render(
        request,
        'hello/category.html',
        {
            'name': SpotipyFunctions.displayname,
            # 'picture': SpotipyFunctions.profile_pic,
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
            # 'picture': SpotipyFunctions.profile_pic,
            'playlist': playlistDisplay
        }
    )
    
def workout(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    workoutObject = workoutPlaylistClass()
    workoutObject.workoutTracks_uri()
    passId = workoutObject.savePlaylist()
    url = workoutObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )

def study(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    studyObject = studyPlaylistClass()
    studyObject.studyTracks_uri()
    passId = studyObject.savePlaylist()
    url = studyObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )

def driving(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    drivingObject = drivingPlaylistClass()
    drivingObject.drivingTracks_uri()
    passId = drivingObject.savePlaylist()
    url = drivingObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )


def yearRange(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/yearRangeChoices.html',
        {
            'playlistName': YearRangePlaylist.playlist_name,
            'playlist': playlistDisplay,
            'name': SpotipyFunctions.displayname
        }
    )

def thirties(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    yearObject = yearRangePlaylistClass()
    passId = yearObject.thirtiesPlaylist()
    url = yearObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )

def fourties(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    yearObject = yearRangePlaylistClass()
    passId = yearObject.fourtiesPlaylist()
    url = yearObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )

def fifties(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    yearObject = yearRangePlaylistClass()
    passId = yearObject.fiftiesPlaylist()
    url = yearObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )

def sixties(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    yearObject = yearRangePlaylistClass()
    passId = yearObject.sixtiesPlaylist()
    url = yearObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )

def seventies(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    yearObject = yearRangePlaylistClass()
    passId = yearObject.SeventiesPlaylist()
    url = yearObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )

def eighties(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    yearObject = yearRangePlaylistClass()
    passId = yearObject.eightiesPlaylist()
    url = yearObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,            
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )

def nineties(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    yearObject = yearRangePlaylistClass()
    passId = yearObject.NinetiesPlaylist()
    url = yearObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )

def millenial(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    yearObject = yearRangePlaylistClass()
    passId = yearObject.millennialPlaylist()
    url = yearObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )

def international(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    intObject = internationalPlaylistClass()
    passId = intObject.internationalPlaylist()
    url = intObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )

def artists(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    return render(
        request,
        'hello/artists.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
        }
    )

def uncleposty(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    raObject = relatedArtistsPlaylistClass()
    raObject.unclepostyPlaylist()
    passId = raObject.savePlaylist()
    url = raObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )

def selenagomez(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    raObject = relatedArtistsPlaylistClass()
    raObject.selenagomezPlaylist()
    passId = raObject.savePlaylist()
    url = raObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )

def rezz(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    raObject = relatedArtistsPlaylistClass()
    raObject.rezzPlaylist()
    passId = raObject.savePlaylist()
    url = raObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )

def atribecalledquest(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    raObject = relatedArtistsPlaylistClass()
    raObject.atribecalledquestPlaylist()
    passId = raObject.savePlaylist()
    url = raObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )

def travisscott(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    raObject = relatedArtistsPlaylistClass()
    raObject.travisscottPlaylist()
    passId = raObject.savePlaylist()
    url = raObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )

def timmcgraw(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    raObject = relatedArtistsPlaylistClass()
    raObject.timmcgrawPlaylist()
    passId = raObject.savePlaylist()
    url = raObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )

def nancyajram(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    raObject = relatedArtistsPlaylistClass()
    raObject.nancyajramPlaylist()
    passId = raObject.savePlaylist()
    url = raObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )

def prince(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    raObject = relatedArtistsPlaylistClass()
    raObject.princePlaylist()
    passId = raObject.savePlaylist()
    url = raObject.showPlaylist(passId)
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )

def surpriseme(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    surpriseObject = surprisePlaylistClass()
    surpriseObject.surpriseSearch()
    passId = surpriseObject.savePlaylist()
    url = surpriseObject.showPlaylist(passId)    
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url
        }
    )