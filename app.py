from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime

HOST = "127.0.0.1"
PORT = 8000

class ClientServerHandler(BaseHTTPRequestHandler):
    def send_json(self, status_code, payload):
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            html = open("index.html", "rb").read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(html)))
            self.end_headers()
            self.wfile.write(html)
        elif self.path == "/api/status":
            self.send_json(200, {
                "status": "success",
                "message": "Client and server are communicating successfully!",
                "server": "Python localhost server",
                "timestamp": datetime.now().isoformat(timespec="seconds")
            })
        else:
            self.send_json(404, {"status": "error", "message": "Endpoint not found"})

    def do_POST(self):
        if self.path != "/api/message":
            self.send_json(404, {"status": "error", "message": "Endpoint not found"})
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
            data = json.loads(self.rfile.read(length).decode("utf-8"))
            message = str(data.get("message", "")).strip()
            if not message:
                self.send_json(400, {"status": "error", "message": "Please enter a message."})
                return

            self.send_json(200, {
                "status": "success",
                "received_message": message,
                "reply": f"Server received your message: {message}",
                "server_time": datetime.now().isoformat(timespec="seconds")
            })
        except (json.JSONDecodeError, UnicodeDecodeError):
            self.send_json(400, {"status": "error", "message": "Invalid JSON request."})

    def log_message(self, format_string, *args):
        print(f"[SERVER] {self.address_string()} - {format_string % args}")

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), ClientServerHandler)
    print(f"Server running at http://{HOST}:{PORT}")
    print("Press Ctrl+C to stop the server.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()
