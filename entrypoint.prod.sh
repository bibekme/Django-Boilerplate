#!/bin/sh
echo "Waiting for postgres..."
while ! nc -z $SETTINGS_DB_HOST $SETTINGS_DB_PORT; do
    sleep 0.1
done
echo "PostgreSQL started"

python manage.py collectstatic --noinput

exec "$@"
