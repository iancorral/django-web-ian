from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.shortcuts import render
from .models import Task
from django.urls import reverse   

# Lista de tareas en memoria
tasks = ["foo", "bar", "baz"]

def index1(request):
    return HttpResponse("<h1>Hello World!</h1>")

def hello(request):
    return HttpResponse("<h1>Hello desde la vista hello!</h1>")

def current_datetime(request):
    now = datetime.now()
    html = f"<h1>Fecha y hora actual:</h1><p>{now.strftime('%Y-%m-%d %H:%M:%S')}</p>"
    return HttpResponse(html)

def greet(request, name):
    return HttpResponse(f"<h1>Hola, {name}!</h1>")

def saludo(request, nombre):
    return render(request, "mi_primera_pagina/saludo.html", {"nombre": nombre.capitalize()})

def index(request):
    return render(request, "mi_primera_pagina/index.html")

def about(request):
    return render(request, "mi_primera_pagina/about.html")

def sumar(request):
    num1 = 5
    num2 = 3
    resultado = num1 + num2
    return render(request, 'mi_primera_pagina/sumar.html', {
        'num1': num1,
        'num2': num2,
        'resultado': resultado
    })

def tasks_index(request):
    return render(request, "mi_primera_pagina/tasks_index.html", {"tasks": tasks})

def tasks_add(request):
    if request.method == "POST":
        task = request.POST.get("task")
        if task:
            tasks.append(task)
        return HttpResponseRedirect(reverse("tasks_index"))  # <-- corregido
    return render(request, "mi_primera_pagina/tasks_add.html")

def tasks_admin_list(request):
    tasks_db = Task.objects.all().order_by("-created_at")
    return render(request, "mi_primera_pagina/tasks_admin_list.html", {"tasks": tasks_db})

def index2(request):
    return render(request, "mi_primera_pagina/index2.html")

def user_profile(request):
    users = User.objects.all() 
    return render(request, "mi_primera_pagina/user.html", {"users": users})