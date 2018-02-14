from flask import Flask
import os
import subprocess
command = "dpkg -l"
app = Flask(__name__)
MESSAGE = os.getenv('MESSAGE', 'Cannot load the env')
SOME_API_KEY = os.getenv('SOME_API_KEY', None)
PACKAGE_LIST = subprocess.check_output(['dpkg','-l'])
SSH_PACKAGE = subprocess.check_output(['grep','ssh-server',PACKAGE_LIST])
@app.route("/")
def hello():
    #return MESSAGE
    return SSH_PACKAGE
if __name__ == "__main__":
    app.run(host='0.0.0.0')
