from flask import Flask
from flask import request
import datetime

testapp = Flask(__name__)

@testapp.get('/')
def index():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'[{timestamp}] {request.remote_addr} {request.method} {request.path}')
    print("--- CONTENT START ---")
    print(request.headers)
    print("--- CONTENT END ---")
    return 'OK'

if __name__ == '__main__':
    host = "0.0.0.0"
    port = 5000
    debug = True
    testapp.run(host=host, port=port, debug=debug)