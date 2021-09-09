#!/usr/bin/env bash

cd dealer/scr && python manage.py migrate && gunicorn djangoProject.wsgi:application -b 0.0.0.0:8000 || { echo 'runserver failed' ; exit 1; }