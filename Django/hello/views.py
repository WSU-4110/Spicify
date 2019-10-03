from django.http import HttpResponse
from hello import SpicifyLogin

def home(request):
    return HttpResponse("Your Name: " + SpicifyLogin.displayname + " --------------- Your Followers: " + str(SpicifyLogin.followers) + "YEEEEt")
