from django.urls import path
# from django.conf.urls import url
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
#     path("about/", views.about, name="about"),
#     path("hello/<name>", views.hello_there, name="hello_there"),
]