FROM php:8.0.7-cli-alpine3.13
# https://hub.docker.com/_/php

RUN mkdir /app
WORKDIR /app
ADD . /app/

EXPOSE 8080

CMD ["php", "-S", "0.0.0.0:8080"]
