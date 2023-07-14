from flask import Flask
from flask import request
import datetime
import argparse

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
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', help='host', default='0.0.0.0')
    parser.add_argument('--port', help='port', default=5000)
    parser.add_argument('--debug', help='debug', default=True)
    args = parser.parse_args()
    host = args.host
    port = int(args.port)
    debug = True if args.debug.lower() == 'true' else False
    testapp.run(host=host, port=port, debug=debug)