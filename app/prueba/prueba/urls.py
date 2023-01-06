"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import prueba.views as vistas
from prueba import settings

urlpatterns = [
    path('%sbotPrueba/' % settings.PATH_PREFIX, vistas.chat_bot_prueba, name='botPrueba'),
    path('%sbotProgAdmon/' % settings.PATH_PREFIX, vistas.chat_bot_prog_admon, name='botProgAdmon'),
    path('%senviar_mensaje/' % settings.PATH_PREFIX, vistas.enviar_mensaje, name='enviar_mensaje'),
    path('%smain/' % settings.PATH_PREFIX, vistas.main, name='main'),
    #path('%s' % settings.PATH_PREFIX, vistas.main, name='main'),
    path('%sbotPracticasIS/' % settings.PATH_PREFIX, vistas.chat_bot_practicasIS, name='botPracticasIS'),
    
]
