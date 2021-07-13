from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():

    _ex_remote_addr = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    msg ='Your Remote IP Address is "{}" .\nHello World!! :)'.format(_ex_remote_addr)
    return msg


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    