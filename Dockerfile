FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/
RUN pip --no-cache-dir install -r /tmp/requirements.txt

WORKDIR /opt/tickers-project
COPY . .

USER root

ENTRYPOINT ["/bin/bash", "/opt/tickers-project/entrypoint.sh"]
