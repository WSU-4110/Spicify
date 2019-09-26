from django.shortcuts import render
import re
from datetime import datetime

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )