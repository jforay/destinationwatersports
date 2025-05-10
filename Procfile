release: python manage.py collectstatic --noinput

web: gunicorn dutchmanCreek.wsgi:application --log-file -
