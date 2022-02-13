from flask import Flask, request
import subprocess
import datetime

app = Flask(__name__)

@app.route("/")
def hello():

    _ex_remote_addr = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    # Comment on standard output in Container.
    subprocess.call(["echo", "Start 10s"])
    # Execute the Sleep command.
    subprocess.call(["sleep", "10"])

    msg ='test is done.\n It is "{}" now.'.format(datetime.datetime.now())

    return msg

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    