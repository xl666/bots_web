import requests
import os


def preprocesar_imgs(texto):
    return '<img class="img-chat" src="%s" />' % texto


def recuperar_contenido_archivo(path):
    res = ''
    with open(path) as archivo:
        res = archivo.read()
    return res


def preprocesar_codigo(texto):
    partes = texto.split(':')
    if len(partes) != 3:
        return texto
    _, lenguaje, path = partes
    plantilla = """
    <pre><code class="language-%s">
%s
    </code></pre>
    """
    path = 'static/codigo/%s' % path
    contenido = recuperar_contenido_archivo(path)
    return plantilla % (lenguaje, contenido)
    
def recolectar_texts(objetos):
    res = []
    for obj in objetos:
        texto = obj.get('text', '')
        if obj.get('image', ''):
            res.append(preprocesar_imgs(obj.get('image', '')))
        elif texto.strip().startswith('code:'):
            contenido = preprocesar_codigo(texto)
            res.append(contenido)
        else:
            res.append(texto)
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
