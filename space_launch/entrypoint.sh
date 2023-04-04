#!/bin/sh

# wait for the database to start up
while ! nc -z db 5432; do
  sleep 0.1
done

# run database migrations
python manage.py migrate --no-input

# start the development server
python manage.py runserver 0.0.0.0:8000