#!/usr/bin/env python3
#
# main.py
#
#########################################################################

import time
from http.server import HTTPServer
from server import Server

HOST_NAME = ''            # any IP address on a machine
PORT_NUMBER = 8000

if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)  # Create server
                                                # link to customized http server
    print(time.asctime(), 'Server UP - %s:%s' % \
        (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()        # Start the server object
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
