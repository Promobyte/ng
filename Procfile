web: gunicorn boilerplate.wsgi --limit-request-line 8188 --log-file -
worker: celery worker --app=boilerplate --loglevel=info
