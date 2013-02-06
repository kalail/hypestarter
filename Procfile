web: python hypestarter/manage.py run_gunicorn --workers=9 --bind=0.0.0.0:$PORT
worker: python hypestarter/manage.py celery worker -B -E --loglevel=INFO
monitor: python hypestarter/manage.py celery flower