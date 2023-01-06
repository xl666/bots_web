from django.template import Template, Context, base
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from modelo import models
import prueba.settings as conf
import datetime
from datetime import timezone
from django.views.decorators.csrf import csrf_exempt
import prueba.peticiones
import os
import base64


def generar_identificador():
    binario = os.urandom(12)
    return base64.b64encode(binario).decode('utf-8')


def main(request):
    return render(request, 'main.html')

def request_proxy(request, template):
    request.session['sender'] = generar_identificador()
    return render(request, template, {'prefijo': conf.PATH_PREFIX})

def chat_bot_prueba(request):
    return request_proxy(request, 'bot_prueba.html')

def chat_bot_prog_admon(request):
    return request_proxy(request, 'prog_admon.html')

def chat_bot_practicasIS(request):
    return request_proxy(request, 'bot_practicasIS.html')

@csrf_exempt
def enviar_mensaje(request):
    if request.method == 'POST':
        mensaje = request.POST.get('mensaje', '').strip()
        host = request.POST.get('host', 'localhost').strip()
        puerto = request.POST.get('puerto', '5002').strip()
        sender = request.session.get('sender', 'bob')
        respuesta = prueba.peticiones.mandar_mensaje(sender, mensaje, host, puerto)
        if respuesta:
            contenido = {"mensaje": mensaje, "respuesta": respuesta}
            return JsonResponse(contenido)
        else:
            contenido = {"mensaje": mensaje, "respuesta": ['No te puedo ayudar con eso']}
            return JsonResponse(contenido)


