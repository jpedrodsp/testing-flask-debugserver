from flask import Flask
from flask import request

testapp = Flask(__name__)

@testapp.get('/')
def index():
    return 'OK'

if __name__ == '__main__':
    host = "0.0.0.0"
    port = 5000
    debug = True
    testapp.run(host=host, port=port, debug=debug)