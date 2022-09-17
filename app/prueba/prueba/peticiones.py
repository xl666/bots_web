import requests
import os

def mandar_mensaje(sender, mensaje, host, puerto):
    BOT_URL = "http://%s:%s" % (host, puerto)
    URI = "/webhooks/rest/webhook"
    data = {'sender': sender, 'message': mensaje}
    try:
        res = requests.post(BOT_URL + URI,
                            json=data)
        return res.json()[0]
    except:
        return None
