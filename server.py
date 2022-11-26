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
                                                body {background-color: #dddddd;}
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
                                    </HTML>"""
                print(routes[self.path])
                self.send_response(status)
                self.send_header('Content-type', content_type)
                #self.send_response(response_content)
                self.end_headers()
                return bytes(response_content,"UTF-8")
                
                #self.end_headers()
            elif self.path =='/system':
                content_type = 'text/html'
                #print(type(routes[self.path]))
                response_content =''
                response_content += """<HTML>
                                            <style>
                                                body {background-color: white;}
                                                h1   {color: Black;}
                                                table {
                                                    font-family: arial, sans-serif;
                                                    border-collapse: collapse;
                                                    width: 100%;
                                                    }

                                                td, th {
                                                    border: 1px solid #dddddd;
                                                    text-align: left;
                                                    padding: 8px;
                                                    }
                                                th{
                                                    background-color: pink;
                                                }
                                                tr:nth-child(even) {
                                                    background-color: pink;
                                                    }
                                            </style>
                                    <h1>System information</h1>"""
                response_content+=f"<Table> <tr>\
                    <th>Info.</th>\
                    <th>Description</th><tr>"
                for i in routes[self.path]:
                    tmp = i.split(' = ')
                    tmp2 = tmp[0].split('SNMPv2-MIB::')
                    response_content+=f'<tr><td>{tmp2[1]}</td><td>{tmp[1]}</td></tr>'
                response_content+="</HTML>"
                print(routes[self.path])
                self.send_response(status)
                self.send_header('Content-type', content_type)
                #self.send_response(response_content)
                self.end_headers()
                return bytes(response_content,"UTF-8")
            elif self.path=='/ip':
                content_type = 'text/html'
                response_content=''
                #print((routes[self.path]))
                response_content += """<HTML>
                                            <style>
                                                body {background-color: white;}
                                                h1   {color: Black;}
                                                p    {color: red;}
                                                table {
                                                    font-family: arial, sans-serif;
                                                    border-collapse: collapse;
                                                    width: 100%;
                                                    }

                                                td, th {
                                                    border: 1px solid #dddddd;
                                                    text-align: left;
                                                    padding: 8px;
                                                    }
                                                tr:nth-child(odd) {
                                                    background-color: #dddddd;
                                                    }
                                            </style>
                                    <H1>IP ROUTE TABLE</H1>"""
                response_content +='<table>\
                    <tr><th>Destination</th>\
                    <th>Interface</th>\
                    <th>Next hop</th>\
                    <th>Routing types</th>\
                    <th>Routing Protocol</th>\
                    <th>Subnet mask</th></tr>'
                """response_content +='<table>\
                    <tr><th>Destination</th>\
                    <th>Interface</th></tr>'"""
                Des=[]
                Int=[]
                Nex=[]
                Typ=[]
                Pro=[]
                Bro=[]
                for i in routes[self.path]:
                    test=i.split(' = ')
                    if  "SNMPv2-SMI::mib-2.4.21.1.1." in  i:
                        tmp = i.split(' = ')
                        #print(tmp[1])
                        Des.append(tmp[1])
                    if  "SNMPv2-SMI::mib-2.4.21.1.2." in  i:
                        tmp = i.split(' = ')
                        #print(tmp[1])
                        Int.append(tmp[1])
                    if  "SNMPv2-SMI::mib-2.4.21.1.7." in  i:
                        tmp = i.split(' = ')
                        #print(tmp[1])
                        Nex.append(tmp[1])
                    if  "SNMPv2-SMI::mib-2.4.21.1.8." in  i:
                        tmp = i.split(' = ')
                        #print(tmp[1])
                        Typ.append(tmp[1])
                    if  "SNMPv2-SMI::mib-2.4.21.1.9." in  i:
                        tmp = i.split(' = ')
                        #print(tmp[1])
                        Pro.append(tmp[1])
                    if  "SNMPv2-SMI::mib-2.4.21.1.11." in  i:
                        tmp = i.split(' = ')
                        #print(tmp[1])
                        Bro.append(tmp[1])
                #tmp= i.split(' = ')
                for i in range (len(Des)):
                    response_content += f'<tr><td>{Des[i]}</td><td>{Int[i]}</td><td>{Nex[i]}</td><td>{Typ[i]}</td><td>{Pro[i]}</td><td>{Bro[i]}</td></tr>'                    
                response_content +='</table></HTML>'
            
                self.send_response(status)
                self.send_header('Content-type', content_type)
                self.end_headers()
                return bytes(response_content,"UTF-8")

            else:
                content_type = 'text/html'
                #print(type(routes[self.path]))
                response_content =''
                response_content += """<HTML>
                                            <style>
                                                body {background-color: white;}
                                                h1   {color: Black;}
                                                table {
                                                    font-family: arial, sans-serif;
                                                    border-collapse: collapse;
                                                    width: 100%;
                                                    }

                                                td, th {
                                                    border: 1px solid #dddddd;
                                                    text-align: left;
                                                    padding: 8px;
                                                    }
                                                th{
                                                    background-color: skyblue;
                                                }
                                                tr:nth-child(even) {
                                                    background-color: skyblue;
                                                    }
                                            </style>
                                    <h1>ICMP Echo</h1>"""
                response_content+=f"<Table> <tr>\
                    <th>Info.</th>\
                    <th>count</th><tr>"
                for i in routes[self.path]:
                    tmp = i.split(' = ')
                    tmp2 = tmp[0].split('SNMPv2-SMI::mib-')
                    response_content+=f'<tr><td>{tmp2[1]}</td><td>{tmp[1]}</td></tr>'
                response_content+="</HTML>"
                print(routes[self.path])
                self.send_response(status)
                self.send_header('Content-type', content_type)
                #self.send_response(response_content)
                self.end_headers()
                return bytes(response_content,"UTF-8")
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
