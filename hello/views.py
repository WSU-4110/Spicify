from django.http import HttpResponse
from hello import SpotipyFunctions
from django.shortcuts import render


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
