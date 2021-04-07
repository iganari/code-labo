# https://github.com/JasonHaley/hello-python/tree/master/app

from flask import Flask, request, render_template
import socket
import datetime
import os

app = Flask(__name__)

@app.route("/")
def hello():
    msg ='Your URL is "{}" .\nHello World!! :)'.format(request.url) 

    return msg 

@app.route("/healthz")
def healthcheak():
    msg ='This is Health Cheak Page.' 

    return msg

# QueryString
@app.route("/qs")
def param():
    name = request.args.get('name')
    age  = request.args.get('age')
    msg  ='Your URL is "{}" .\nname: {}\nage: '.format(request.url, name, age)

    # return msg
    return render_template('hello2.html', name=name)


@app.route('/<mypath>')
def show_path(mypath):
    your_environ = os.environ
    # your_environ = os.environ['PATH']
    msg ='Your URL is "{}" .\nHostName: {}\nIP: {}\nCurrent time: {}\nYour Env: {}'.format(request.url, host_name, host_ip, current_time, your_environ) 

    return msg 


if __name__ == "__main__":
    host_name    = socket.gethostname()
    host_ip      = socket.gethostbyname(host_name)
    current_time = datetime.datetime.now()

    app.run(debug=True, host='0.0.0.0', port=5000)
    