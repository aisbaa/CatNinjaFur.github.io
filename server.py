import socketserver
from http.server import SimpleHTTPRequestHandler

class HTMLHandler(SimpleHTTPRequestHandler):
    def do_get(self):
        return None

if __name__ == '__main__':
    PORT = 8080
    with socketserver.TCPServer(("", PORT), HTMLHandler) as httpd:
        print("Listening on port {}. Press Ctrl+C to stop.".format(PORT))
        httpd.serve_forever()

