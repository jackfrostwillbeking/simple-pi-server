from flask import Flask
import os
import subprocess

app = Flask(__name__)
MESSAGE = os.getenv('MESSAGE', 'Cannot load the env')
SOME_API_KEY = os.getenv('SOME_API_KEY', None)
SSH_PACKAGE = subprocess.check_output(['dpkg','-l','openssh-server'])
@app.route("/")
def hello():
    #return MESSAGE
    return SSH_PACKAGE
if __name__ == "__main__":
    app.run(host='0.0.0.0')
