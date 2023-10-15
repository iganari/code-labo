FROM python:3.11.6-alpine3.18
# https://hub.docker.com/_/python/tags?page=1&name=-alpine

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "/app/main.py"]
