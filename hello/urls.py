from django.urls import path
from hello import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("", views.category, name="category"),
    path("layout", views.layout, name="layout"),    
]
