FROM node:18.14.0

WORKDIR /app

ADD ./vaultsync.py /app/vaultsync.py

RUN npm install -g @bitwarden/cli
RUN apt update && \
    apt install jq -y
