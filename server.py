#########################################################
# server.py
#########################################################

from http.server import BaseHTTPRequestHandler
from importlib.resources import path
from posixpath import split
from route import routes
from pathlib import Path
from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.hlapi import *  
import mysql.connector
import test
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=test.x,
  database = 'net_man'
)
IR=[]
IE=[]
OR=[]
OE=[]
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
                response_content+="<div>"
                response_content+=f"<Table> <tr>\
                    <th>Info.</th>\
                    <th>count</th><tr>"
                
                #print(routes[self.path])
                result=[]

                errorIndication, errorStatus, errorIndex, varBinds = next(
                    getCmd(SnmpEngine(),
                        CommunityData('public'),
                        UdpTransportTarget(('127.0.0.1', 161)),
                        ContextData(),
                        #icmpInEchos
                        ObjectType(ObjectIdentity('1.3.6.1.2.1.5.8.0')),
                        #icmpInEchosReq
                        ObjectType(ObjectIdentity('1.3.6.1.2.1.5.9.0')),
                        #icmpOutEchos
                        ObjectType(ObjectIdentity('1.3.6.1.2.1.5.21.0')),
                        #icmpOutEchosReps
                        ObjectType(ObjectIdentity('1.3.6.1.2.1.5.22.0')))
                )

                if errorIndication:
                    print(errorIndication)
                elif errorStatus:
                    print('%s at %s' % (errorStatus.prettyPrint(),
                                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
                else:
                    for varBind in varBinds:
                        #print(' = '.join([x.prettyPrint() for x in varBind]))
                        result.append(str(varBind))
                        
                global IE
                global OE
                global IR
                global OR
                mycursor = mydb.cursor()
                mycursor.execute('USE net_man;')
                for i in result:
                    
                    tmp = i.split(' = ')
                    tmp2 = tmp[0].split('SNMPv2-SMI::mib-')
                    if "2.5.8.0" in i :
                        response_content+=f'<tr><td>ICMPInEchos ({tmp2[1]})</td><td>{tmp[1]}</td></tr>'
                        sql = "INSERT INTO Echo_icmp (name, amount) VALUES (%s, %s)"
                        mycursor.execute(sql, (tmp2[1],tmp[1]))
                        #print('success add IE')
                        #IE.append(int(tmp[1]))
                        #print(IE)
                    if "2.5.9.0" in i :
                        response_content+=f'<tr><td>ICMPInEchosReps ({tmp2[1]})</td><td>{tmp[1]}</td></tr>'
                        #IR.append(int(tmp[1]))
                        sql = "INSERT INTO Echo_icmp (name, amount) VALUES (%s, %s)"
                        mycursor.execute(sql, (tmp2[1],tmp[1]))
                        #print('success add IR')
                        #IR+=str(tmp[1])+','
                    if "2.5.21.0" in i :
                        response_content+=f'<tr><td>ICMPOutEchos ({tmp2[1]})</td><td>{tmp[1]}</td></tr>'
                        #OE.append(int(tmp[1]))
                        sql = "INSERT INTO Echo_icmp (name, amount) VALUES (%s, %s)"
                        mycursor.execute(sql, (tmp2[1],tmp[1]))
                        #print('success add OE')
                        #OE+=str(tmp[1])+','
                    if "2.5.22.0" in i :
                        response_content+=f'<tr><td>ICMPOutEchosReps ({tmp2[1]})</td><td>{tmp[1]}</td></tr>'
                        sql = "INSERT INTO Echo_icmp (name, amount) VALUES (%s, %s)"
                        mycursor.execute(sql, (tmp2[1],tmp[1]))
                        #print('success add OR')
                        #OR.append(int(tmp[1]))
                        
                        #OR+=str(tmp[1])+','
                mycursor.execute('Select * from Echo_icmp;')
                result = mycursor.fetchall()
                for i in result:

                    tmp = str(i).split("'")
                    if "2.5.8.0" in tmp[1] :
                        IE.append(tmp[3])
                    elif "2.5.9.0" in i :
                        IR.append(tmp[3])
                    elif "2.5.21.0" in i :
                        OE.append(tmp[3])
                    elif "2.5.22.0" in i :
                        OR.append(tmp[3])
                #print(IR)
                time=[]
                for i in range(0,len(IE)):
                    time.append(i)
                response_content+="</div>"
                response_content+='<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>\
                    <canvas id="myChart" style="width:100%;max-width:600px"></canvas>\
                    <script>\
                    var xValues = [1,2,3,4,5,6,7,8,9,10];\
                    new Chart("myChart", {\
                    type: "line",\
                    data: {\
                        labels: xValues,\
                        datasets: [{ \
                        data: '+str(IE)+',\
                        borderColor: "red",\
                        fill: false\
                        }, { \
                        data: '+str(IR)+',\
                        borderColor: "blue",\
                        fill: false\
                        }, { \
                        }, { \
                        data: '+str(OE)+',\
                        borderColor: "green",\
                        fill: false\
                        }, { \
                        data: '+str(OR)+',\
                        borderColor: "black",\
                        fill: false\
                        }]\
                    },'
                   
                response_content+="options: {\
                legend: {display: true,\
   			    }\
                }\
                });\
                </script>\
                </HTML>"
                self.send_response(status)
                self.send_header('Content-type', content_type)
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
