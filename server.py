from http.server import HTTPServer, BaseHTTPRequestHandler
import ujson
from io import BytesIO

with open('config.py') as filepointer:
     secrets = ujson.loads(filepointer.read())


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

   # def do_GET(self):
   #     self.send_response(200)
   #     self.end_headers()
   #     self.wfile.write(b'Hello, world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


httpd = HTTPServer((secrets['server_address'], 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
