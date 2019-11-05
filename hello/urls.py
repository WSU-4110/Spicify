from django.urls import path
from hello import views

urlpatterns = [
    path("home", views.home, name="home"),
    path('home/', views.home, name='home'),
    path("", views.category, name="category"),
    path("workout", views.workout, name="workout"),
    path("study", views.study, name="study" ),
    path("driving", views.driving, name="driving"),
    path("yearRange", views.yearRange, name="yearRange"),
    path("thirty", views.thirties, name="thirty"),
    path("fourty", views.fourties, name="fourty"),
    path("fifty", views.fifties, name="fifty"),
    path("sixty", views.sixties, name="sixty"),
    path("seventy", views.seventies, name="seventy"),
    path("eighty", views.eighties, name="eighty"),
    path("ninety", views.nineties, name="ninety"),
    path("millenial", views.millenial, name="millenial"),
    path("international", views.international, name="international"),       
]
