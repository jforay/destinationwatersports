release: python manage.py collectstatic --noinput

web: gunicorn destinationwatersports.wsgi:application --log-file -
