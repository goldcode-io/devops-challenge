import os
import json
import subprocess
from flask import Flask
from flask import request
from subprocess import PIPE, Popen

app = Flask(__name__)
app.debug = True

@app.route('/healthcheck')
def status():
    resp = {
        "Status":"heart beating steady and strong"
    }
    response = app.response_class(
        response=json.dumps(resp),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/') 
def main():
    resp = {
        "App Test":"Alive"
    }
    response = app.response_class(
        response=json.dumps(resp),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8888)