from enum import unique
from django.db import models

class Peticion(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    intentos = models.IntegerField(default=1)
    timestamp = models.DateTimeField()
