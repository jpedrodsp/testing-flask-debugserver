# Temporary Flask Debug Server

## Getting Started

To execute the server, install the needed dependencies and run the server.

For instance, on Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python server.py
```

You can pass additional flags to the server:

- `--host`: The host to listen on (default: "0.0.0.0", which means all available interfaces)
- `--port`: The port to listen on (default: 5000)
- `--debug`: Enable debug mode (default: True)

## Endpoints

### GET /
Returns a simple "OK" message.