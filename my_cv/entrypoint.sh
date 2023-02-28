#!/bin/sh

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate --noinput

echo "start gunicorn"
gunicorn --bind 0.0.0.0:5005 --workers 3 my_cv.wsgi:application