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

Messages will be logged to the console.
The content messages will be printed with a guard to make them easier to find.

For instance:

```
[2023-07-14 17:07:32] 127.0.0.1 GET /
--- CONTENT START ---
Host: localhost:5000
Connection: keep-alive
Sec-Ch-Ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7,de-DE;q=0.6,de;q=0.5


--- CONTENT END ---
```

## Endpoints

### GET /
Returns a simple "OK" message.