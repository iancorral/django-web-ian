from django.http import HttpResponse
from datetime import datetime

def index(request):
    return HttpResponse("<h1>Hello World!</h1>")

def hello(request):
    return HttpResponse("<h1>Hello desde la vista hello!</h1>")

def current_datetime(request):
    now = datetime.now()
    html = f"<h1>Fecha y hora actual:</h1><p>{now.strftime('%Y-%m-%d %H:%M:%S')}</p>"
    return HttpResponse(html)

def greet(request, name):
    return HttpResponse(f"<h1>Hola, {name}!</h1>")
