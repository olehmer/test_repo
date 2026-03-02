#!/usr/bin/env python3
"""Simple Python web server listening on localhost."""

from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(b"""<!DOCTYPE html>
<html>
<head><title>Simple Python Web Server</title></head>
<body>
  <h1>Hello from Python!</h1>
  <p>Your simple web server is running.</p>
</body>
</html>""")

    def log_message(self, format, *args):
        pass  # suppress request logs


if __name__ == "__main__":
    host, port = "localhost", 8080
    server = HTTPServer((host, port), Handler)
    print(f"Serving at http://{host}:{port}")
    server.serve_forever()
