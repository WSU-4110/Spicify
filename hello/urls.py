from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path('home/', views.home, name='home'),
    path("category", views.category, name="category"),
    path("workout", views.workout, name="workout"),
    path("study", views.study, name="study" )
]
