from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_primera_pagina.urls')),  # 👈 Aquí se conecta tu app
]
