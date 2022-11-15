#########################################################
# server.py
#########################################################

from http.server import BaseHTTPRequestHandler
from route import routes
from pathlib import Path
from pysnmp.entity.rfc3413.oneliner import cmdgen  
class Server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return
    def do_POST(self):
        return
    
    def do_GET(self):
        self.respond()
        
    def handle_http(self):
        status = 200
        content_type = 'text/plain'
        #print(checker)
            
        if self.path in routes:
            content_type = 'text/plain'
            print(type(routes[self.path]))
            response_content = f'{routes[self.path]}'
            #esponse_content = f'{routes[self.path]}'
            
            print(routes[self.path])
            #checker=True
           
        else:
            status = 404
            response_content = 'Page not found'      

        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()
        
        return bytes(response_content, "UTF-8")

    def respond(self):
        content = self.handle_http()
        self.wfile.write(content)
        return
