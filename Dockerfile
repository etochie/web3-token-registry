FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /var/opt/web3-token-registry
# Args
ARG SHORT_SHA

WORKDIR /var/opt/web3-token-registry

# Adding Pipfiles
COPY ./requirements.txt /tmp/

# Installing dependencies
RUN pip --no-cache-dir install -r /tmp/requirements.txt

COPY app .

# Generate version file
RUN sed -i "s|YYYYMMDD|$(date '+%Y%m%d')|g" ./core/version.py && \
    sed -i "s|SHORT_SHA|${SHORT_SHA}|g" ./core/version.py

RUN groupadd -r web3-token-registry \
 && useradd --no-log-init -r -g web3-token-registry web3-token-registry \
 && chown -R web3-token-registry:web3-token-registry .

USER web3-token-registry:web3-token-registry

CMD python main.py