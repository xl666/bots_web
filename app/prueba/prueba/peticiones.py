import requests
import os


def preprocesar_imgs(texto):
    return '<img class="img-chat" src="%s" />' % texto


def preprocesar_codigo(texto):
    partes = texto.split(':')
    if len(partes) != 3:
        return texto
    _, lenguaje, path = partes
    pass


def recolectar_texts(objetos):
    res = []
    for obj in objetos:
        if obj.get('image', ''):
            res.append(preprocesar_imgs(obj.get('image', '')))
        else:
            res.append(obj.get('text', ''))
    return res


def mandar_mensaje(sender, mensaje, host, puerto):
    BOT_URL = "http://%s:%s" % (host, puerto)
    URI = "/webhooks/rest/webhook"
    data = {'sender': sender, 'message': mensaje}
    try:
        res = requests.post(BOT_URL + URI,
                            json=data)
        return recolectar_texts(res.json())
    except:
        return None
