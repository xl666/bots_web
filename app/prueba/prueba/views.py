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


def chat(request):
    request.session['sender'] = generar_identificador()
    return render(request, "chat.html")

@csrf_exempt
def enviar_mensaje(request):
    if request.method == 'POST':
        mensaje = request.POST.get('mensaje', '').strip()
        sender = request.session.get('sender', 'bob')
        respuesta = prueba.peticiones.mandar_mensaje(sender, mensaje)
        if respuesta:
            contenido = {"mensaje": mensaje, "respuesta": respuesta['text']}
            return JsonResponse(contenido)
        else:
            contenido = {"mensaje": mensaje, "respuesta": 'No te puedo ayudar con eso'}
            return JsonResponse(contenido)

