FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /var/opt/web3-token-registry
# Args
ARG SHORT_SHA

WORKDIR /var/opt/web3-token-registry

# Adding Pipfiles
COPY Pipfile Pipfile.lock ./

# Installing dependencies
RUN apt-get update && apt-get install -y gcc && \
 pip install pipenv && \
 pipenv install --dev --system --deploy --ignore-pipfile && \
 apt-get purge -y gcc pipenv && \
 apt-get autoremove -y && \
 rm -rf /var/lib/apt/lists/*

COPY app .

# Generate version file
RUN sed -i "s|YYYYMMDD|$(date '+%Y%m%d')|g" ./core/version.py && \
    sed -i "s|SHORT_SHA|${SHORT_SHA}|g" ./core/version.py

RUN groupadd -r web3-token-registry \
 && useradd --no-log-init -r -g web3-token-registry web3-token-registry \
 && chown -R web3-token-registry:web3-token-registry .

USER web3-token-registry:web3-token-registry

CMD python main.py