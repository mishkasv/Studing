#!/usr/bin/env bash

cd dealer && celery -A src.common.celery worker -l info --concurrency=2