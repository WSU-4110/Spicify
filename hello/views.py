from django.http import HttpResponse
from django.shortcuts import render
from hello.models import Login
import requests

def home(request):
    login = Login.SpotifyLogin
    context = {'login': login}
    return render(request, 'hello/home.html', context)

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
    return render(request, 'hello/workout.html', context)
     
    
