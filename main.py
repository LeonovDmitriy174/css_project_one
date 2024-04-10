from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from config import HTML_DOC

hostName = 'localhost'
serverPort = 8000


class MyServer(BaseHTTPRequestHandler):

    def __get_html_content(self):
        with open(HTML_DOC, encoding='utf-8') as html_file:
            file_code = html_file.read()
            return file_code

    def do_GET(self):
        parse_components = parse_qs(urlparse(self.path).query)
        print(parse_components)
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(page_content, 'utf-8'))


if __name__ == '__main__':

    httpd = HTTPServer((hostName, serverPort), MyServer)
    print("serving started http://%s:%s" % (hostName, serverPort))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print("serving stopped")
