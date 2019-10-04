from django.shortcuts import render
from django.http import HttpResponse
from hello import SpicifyLogin
import re

def home(request):
    return render(request, "hello/home.html")
