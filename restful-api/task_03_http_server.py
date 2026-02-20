#!/usr/bin/python3
"""Simple HTTP API using http.server"""

import http.server
import socketserver
import json
from urllib.parse import urlparse

PORT = 8000


class Handler(http.server.BaseHTTPRequestHandler):
    """Basic HTTP request handler class"""

    def do_GET(self):
        """Handle GET requests sent to the server"""
        
        # Parse the requested URL
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        # Root endpoint
        if path == "/":
            # Send HTTP status code 200 (OK)
            self.send_response(200)
            # Define response content type
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            # Send response body
            self.wfile.write(b"Hello, this is a simple API!")

        # JSON data endpoint
        elif path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            # Convert dictionary to JSON and encode to bytes
            response = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(response).encode())

        # Status endpoint
        elif path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # Info endpoint returning JSON metadata
        elif path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            response = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(response).encode())

        # Handle unknown endpoints
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


# Create and start the TCP server
with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
    print(f"Server running on http://localhost:{PORT}")
    httpd.serve_forever()