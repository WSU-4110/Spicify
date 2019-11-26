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
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/category.html',
        {
            'name': SpotipyFunctions.displayname,
            'picture': profile_pic,
            'playlist': playlistDisplay,
        }
    )

def layout(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/layout.html',
        {
            'name': SpotipyFunctions.displayname,
            'picture': profile_pic,
            'playlist': playlistDisplay,
        }
    )
    
def workout(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    workoutObject = workoutPlaylistClass()
    workoutObject.workoutTracks_uri()
    passId = workoutObject.savePlaylist()
    url = workoutObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': profile_pic,
        }
    )

def study(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    studyObject = studyPlaylistClass()
    studyObject.studyTracks_uri()
    passId = studyObject.savePlaylist()
    url = studyObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': profile_pic,
        }
    )

def driving(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    drivingObject = drivingPlaylistClass()
    drivingObject.drivingTracks_uri()
    passId = drivingObject.savePlaylist()
    url = drivingObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': profile_pic,
        }
    )


def yearRange(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/yearRangeChoices.html',
        {
            'playlistName': YearRangePlaylist.playlist_name,
            'playlist': playlistDisplay,
            'name': SpotipyFunctions.displayname,
            'picture': SpotipyFunctions.profile_pic,

        }
    )

def thirties(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    yearObject = yearRangePlaylistClass()
    passId = yearObject.thirtiesPlaylist()
    url = yearObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url,
            'picture': profile_pic,
        }
    )

def fourties(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    yearObject = yearRangePlaylistClass()
    passId = yearObject.fourtiesPlaylist()
    url = yearObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': profile_pic,
        }
    )

def fifties(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    yearObject = yearRangePlaylistClass()
    passId = yearObject.fiftiesPlaylist()
    url = yearObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': profile_pic,
        }
    )

def sixties(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    yearObject = yearRangePlaylistClass()
    passId = yearObject.sixtiesPlaylist()
    url = yearObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': profile_pic,
        }
    )

def seventies(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    yearObject = yearRangePlaylistClass()
    passId = yearObject.SeventiesPlaylist()
    url = yearObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': profile_pic,
        }
    )

def eighties(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    yearObject = yearRangePlaylistClass()
    passId = yearObject.eightiesPlaylist()
    url = yearObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,            
            'playlist': playlistDisplay,
            'playlistUrl': url,
            'picture': profile_pic,
        }
    )

def nineties(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    yearObject = yearRangePlaylistClass()
    passId = yearObject.NinetiesPlaylist()
    url = yearObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': profile_pic,
        }
    )

def millenial(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    yearObject = yearRangePlaylistClass()
    passId = yearObject.millennialPlaylist()
    url = yearObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()    
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': profile_pic,
        }
    )

def international(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    intObject = internationalPlaylistClass()
    passId = intObject.internationalPlaylist()
    url = intObject.showPlaylist(passId)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'playlistUrl': url,
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'picture': profile_pic,
        }
    )

def artists(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/artists.html',
        {
            'name': SpotipyFunctions.displayname,
            'picture': profile_pic,
            'playlist': playlistDisplay,
        }
    )

def uncleposty(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    raObject = relatedArtistsPlaylistClass()
    passId = raObject.unclepostyPlaylist()
    url = raObject.showPlaylist(passId)
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url,
            'picture': profile_pic,
        }
    )

def selenagomez(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    raObject = relatedArtistsPlaylistClass()
    passId = raObject.selenagomezPlaylist()
    url = raObject.showPlaylist(passId)
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url,
            'picture': profile_pic,

        }
    )

def rezz(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    raObject = relatedArtistsPlaylistClass()
    passId = raObject.rezzPlaylist()
    url = raObject.showPlaylist(passId)
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url,
            'picture': profile_pic,
        }
    )

def atribecalledquest(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    raObject = relatedArtistsPlaylistClass()
    passId = raObject.atribecalledquestPlaylist()
    url = raObject.showPlaylist(passId)
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url,
            'picture': profile_pic,
        }
    )

def travisscott(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    raObject = relatedArtistsPlaylistClass()
    passId = raObject.travisscottPlaylist()
    url = raObject.showPlaylist(passId)
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url,
            'picture': profile_pic,
        }
    )

def timmcgraw(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    raObject = relatedArtistsPlaylistClass()
    passId = raObject.timmcgrawPlaylist()
    url = raObject.showPlaylist(passId)
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url,
            'picture': profile_pic,
        }
    )

def nancyajram(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    raObject = relatedArtistsPlaylistClass()
    passId = raObject.nancyajramPlaylist()
    url = raObject.showPlaylist(passId)
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url,
            'picture': profile_pic,
        }
    )

def prince(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    raObject = relatedArtistsPlaylistClass()
    passId = raObject.princePlaylist()
    url = raObject.showPlaylist(passId)
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'picture': profile_pic,
            'playlist': playlistDisplay,
            'playlistUrl': url,
        }
    )
      
def rate(request):
    rating = request.GET['rate']
    SpotipyFunctions.ratePlaylists(rating)
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    profile_pic = SpotipyFunctions.getProfilePic()
    return render(
        request,
        'hello/category.html',
        {
            'name': SpotipyFunctions.displayname,
            'picture': profile_pic,
            'playlist': playlistDisplay,
        }
    )

def surpriseme(request):
    playlistDisplay = SpotipyFunctions.presentPlaylists()
    surpriseObject = surprisePlaylistClass()
    passId = surpriseObject.savePlaylist()
    url = surpriseObject.showPlaylist(passId)
    profile_pic = SpotipyFunctions.getProfilePic()    
    return render(
        request,
        'hello/playlist_view.html',
        {
            'name': SpotipyFunctions.displayname,
            'playlist': playlistDisplay,
            'playlistUrl': url,
            'picture': profile_pic,
        }
    )