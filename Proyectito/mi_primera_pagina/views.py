from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime  # Import necesario

def index(request):
    return HttpResponse("Hello World!")

# NUEVA FUNCIÓN
def current_datetime(request):
    now = datetime.now()
    formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
    return HttpResponse(f"La fecha y hora actual es: {formatted_date}")

def greet_user(request, name):
    return HttpResponse(f"Hola, {name}! Bienvenido a mi proyecto Django.")
