from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),                  # Ruta principal
    path("hello/", views.hello, name='hello'),            # Hello World
    path("datetime/", views.current_datetime, name='datetime'),  # Fecha y hora
    path("greet/<str:name>/", views.greet, name='greet'), # Saludo dinámico
    path("saludo/<str:nombre>/", views.saludo, name='saludo'), # Saludo con template
]