import requests
import os

BOT_URL = "http://localhost:9001"

def mandar_mensaje(sender, mensaje):
    URI = "/webhooks/rest/webhook"
    data = {'sender': sender, 'message': mensaje}
    try:
        res = requests.post(BOT_URL + URI,
                            json=data)
        return res.json()[0]
    except:
        return None
