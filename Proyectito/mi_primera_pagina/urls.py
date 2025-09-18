from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("datetime/", views.current_datetime, name='current_datetime'),
    path("greet/<str:name>/", views.greet_user, name='greet_user'),
]