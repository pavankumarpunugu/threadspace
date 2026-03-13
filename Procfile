web: python manage.py makemigrations posts && python manage.py migrate && gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
