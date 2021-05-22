# https://github.com/JasonHaley/hello-python/tree/master/app

from flask import Flask, request, Response
import socket
import datetime
import os
import json

app = Flask(__name__)

@app.route("/")
def hello():
    msg ='Your URL is "{}" .\nHello World!! :)'.format(request.url)
    return msg 


@app.route("/healthz")
def healthcheak():
    return Response(response=json.dumps({'message': 'health check page'}), status=200)


@app.route('/<mypath>')
def show_path(mypath):
    my_environ = os.environ
    msg ='Your URL is "{}" .\nHostName: {}\nIP: {}\nCurrent time: {}\nYour Env: {}'.format(request.url, host_name, host_ip, current_time, my_environ)
    return msg 


if __name__ == "__main__":
    host_name    = socket.gethostname()
    host_ip      = socket.gethostbyname(host_name)
    current_time = datetime.datetime.now()

    app.run(debug=True, host='0.0.0.0', port=5000)
    