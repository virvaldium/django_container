#!/bin/bash

cd /opt/django_container

# это костыль. По идее тут надо дождаться открытия порта от БД
sleep 10

if [ ! -f "$ENV_FILE" ]; then
   cp example.env .env
fi

echo "Apply database migrations"
python manage.py migrate

echo "Collect static files"
yes yes | python manage.py collectstatic

echo "Starting server"
uwsgi --ini /opt/django_container/configs/uwsgi.docker.ini