#!/usr/bin/env bash

sleep 15

python -u manage.py makemigrations
python -u manage.py migrate

gunicorn --bind :8000 prueba.wsgi:application --reload
