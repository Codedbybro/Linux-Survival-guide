from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import time

last_message = ""

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/hello":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"HELLO FROM BACKEND")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"NOT FOUND")

    def do_POST(self):
        global last_message

        if self.path == "/contact":

            length = int(self.headers['Content-Length'])
            body = self.rfile.read(length).decode()
            data = parse_qs(body)

            name = data.get("name", [""])[0]
            email = data.get("email", [""])[0]
            message = data.get("message", [""])[0]

            current = name + email + message

            # анти-спам (одинаковые запросы)
            if current == last_message:
                self.send_response(429)
                self.end_headers()
                self.wfile.write(b"Too many requests")
                return

            last_message = current

            # лог в файл
            with open("messages.txt", "a") as f:
                f.write("\n---\n")
                f.write(f"Time: {time.ctime()}\n")
                f.write(f"Name: {name}\n")
                f.write(f"Email: {email}\n")
                f.write(f"Message: {message}\n")

            print("NEW MESSAGE RECEIVED")

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Message saved")

server = HTTPServer(("127.0.0.1", 3000), Handler)

print("Server started on 3000...")
server.serve_forever()
