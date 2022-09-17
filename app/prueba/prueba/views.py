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

def enviar_formulario(request):
    """
    Ejemplo de vista con limite de intentos.

    Keyword Arguments:
    request --
    returns: HTTP_Response
    """  
    if request.method == 'GET':
        t = 'envio.html'
        return render(request, t)
    elif request.method == 'POST':
        # actualizar pentciones de ip
        if puede_hacer_peticion(get_client_ip(request)):
            return HttpResponse('OK')
        else:
            return HttpResponse('Intentos agotados')

def login(request):
    request.session['logueado'] = True
    request.session['contador'] = 0
    return HttpResponse('Ya te logueaste')

def pagina_restringida(request):
    contador = request.session.get('contador', '')
    if contador != '':
        request.session['contador'] = contador + 1
    if request.session.get('logueado', False) == True:
        return HttpResponse('Puedes entrar %s' % contador)
    else:
        return HttpResponse('Estás bloqueado %s' % contador)


def logout(request):
    request.session['logueado'] = False
    request.session.flush()
    return redirect('/enviar')
