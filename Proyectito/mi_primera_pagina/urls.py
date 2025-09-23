from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),                  # Ruta principal
    path("index1/", views.index1, name='index1'),         # Nueva ruta
    path("hello/", views.hello, name='hello'),            # Hello World
    path("datetime/", views.current_datetime, name='datetime'),  # Fecha y hora
    path("greet/<str:name>/", views.greet, name='greet'), # Saludo dinámico
    path("<str:nombre>/", views.saludo, name='saludo'), # Saludo con template
    path("about/", views.about, name='about'),            # About page
    path("sumar/", views.sumar, name='sumar'),            # Sumar dos números
]