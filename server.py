#########################################################
# server.py
#########################################################

from http.server import BaseHTTPRequestHandler
from importlib.resources import path
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
            if self.path=='/':
                content_type = 'text/html'
                #print(type(routes[self.path]))
                response_content = """<HTML>
                                            <style>
                                                body {background-color: powderblue;}
                                                h1   {color: Red;}
                                                p    {color: red;}
                                            </style>
                                    <H1>Network Management Web application Base</H1>
                                    <h2>System Infomation</h2>
                                    <button type="button"><a href="/system">System</a></button>
                                    <h2>IP route table</h2>
                                    <button type="button"><a href="/ip">IP</a></button>
                                    <h2>IP ICMP</h2>
                                    <button type="button"><a href="/icmp">ICMP</a></button>
                                    </HTML>"""#f'{routes[self.path]}\n shiba'

                
                
                #esponse_content = f'{routes[self.path]}'
                
                print(routes[self.path])
                self.send_response(status)
                self.send_header('Content-type', content_type)
                #self.send_response(response_content)
                self.end_headers()
                return bytes(response_content,"UTF-8")
                #self.end_headers()
                
            else:
                content_type = 'text/plain, text/html'
                print(type(routes[self.path]))
                print('MIB info')
                #response_content = f'{routes[self.path]}'
                tmp=''
                #dec = routes[self.path].
                for i in routes[self.path]:

                    tmp = tmp+i+'\n'
                    #print(tmp)
                response_content = tmp
                self.send_response(status)
                self.send_header('Content-type', content_type)
                #self.end_headers()S
                return bytes(response_content, "utf-8")
            #checker=True
           
        else:
            status = 404
            response_content = 'Page not found'   
            self.send_response(status)
            self.send_header('Content-type', content_type)
            self.end_headers()
            return bytes(response_content, "UTF-8")   
        #return bytes(response_content, 'UTF-8')
       
        
        

    def respond(self):
        content = self.handle_http()
        self.wfile.write(content)
        return
