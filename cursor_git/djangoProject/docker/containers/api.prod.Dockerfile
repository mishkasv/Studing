FROM python:3.9-slim

RUN apt-get update && apt-get install -y gettext

ADD . /dealer

RUN chmod +x /dealer/docker/scripts/api.entrypoint.prod.sh && \
    chmod +x /dealer/docker/scripts/wait-for-it.sh

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /dealer/requirements/prod.txt