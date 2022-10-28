from http.server import HTTPServer, BaseHTTPRequestHandler
import llc


httpd = None
SimpleHTTPRequestHandler_r = BaseHTTPRequestHandler

@llc.llctype(func_name="server/server")
def http_server(host="localhost", port=80):
    global httpd
    httpd = (host, port)

@llc.llctype(func_name="server/get")
def http_get(text, response_code=200):
    global SimpleHTTPRequestHandler_r
    class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(response_code)
            self.send_header('content-type','text/html')
            self.end_headers()
            self.wfile.write(bytes(text, encoding = 'utf-8'))
    SimpleHTTPRequestHandler_r = SimpleHTTPRequestHandler

    print("ok")

@llc.llctype(func_name="server/start")
def http_start():
    shttpd = HTTPServer(httpd, SimpleHTTPRequestHandler_r)
    print(f"server started at http://{httpd[0]}:{httpd[1]}")
    shttpd.serve_forever()
