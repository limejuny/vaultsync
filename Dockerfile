FROM node:18.14.0

WORKDIR /app

RUN npm install -g @bitwarden/cli
