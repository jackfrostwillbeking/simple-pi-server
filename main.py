from flask import Flask
import os
import subprocess
app = Flask(__name__)
MESSAGE = os.getenv('MESSAGE', 'Cannot load the env')
SOME_API_KEY = os.getenv('SOME_API_KEY', None)

@app.route("/")
def hello():
    test = subprocess.call('dpkg -l|grep openssh-server', shell=True)
    return test

if __name__ == "__main__":
    app.run(host='0.0.0.0')
