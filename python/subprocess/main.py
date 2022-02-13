from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/")
def hello():

    _ex_remote_addr = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    subprocess.call(["echo", "Start 10s"])
    subprocess.call(["sleep", "10"])
    msg ='Your Remote IP Address is "{}" .\nHello World!! :)'.format(_ex_remote_addr)
    return 'test done'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    