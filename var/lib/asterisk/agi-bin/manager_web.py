#!/usr/bin/python
'''minmal AMI client'''

import socket
import sys
import BaseHTTPServer
import cgi
from SimpleHTTPServer import SimpleHTTPRequestHandler

#create an socket
sock = socket.socket()
#now connect to manager on default port 5038
sock.connect(("localhost", 5038))

#send auth creds to login
sock.send("action: login\r\n")
sock.send("username: user\r\n")
sock.send("secret: password\r\n\r\n")

while True:
   #receive response
   line = ''
   response = ''
   while (line[-4:] != '\r\n\r\n'):
      line = sock.recv(1024)
      response += line

   print response

#close the socket
#sock.close()

"""
# Web Server

#overricde do_POST
class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
   def do_POST(self):
      #get args from query string
      self.query_string = self.rfile.read(int(self.headers['Content-Length']))
      self.args = dict(cgi.parse_qsl(self.query_string))
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      #redirect output to browser
      sys.stdout = self.wfile
      #handle the post
      self.wfile.write("<h2>Handling Post</h2><P>")
      self.wfile.write("<li>Location: <b>%s</b>"%(self.path))
      self.wfile.write("<li>Arguments:<b>%s</b><hr>" % (self.args))
      #exectue the script remotely
      execfile(self.path, self.args)

   def do_GET(self):
      self.send_response(200)
      self.send_header('Content-type', 'text/html; charset=utf-8')
      self.end_headers()
      self.wfile.write('''
      <!DOCTYPE html>
      <html>
      <head>
      </head>
      <body>
      <h1><a href="http://192.168.79.103:8000">Web Page</a></h1>
      <h2>%s</h2>
      <p>Some copy here</p>
      <form action="http://192.168.79.103:8000" method="POST">
      Phone #: <input type="text" name="number">
      <input type="submit" value="Submit">
      </body>
      </html>''' % self.path)

#Create the httpd server object
#HandlerClass = SimpleHTTPRequestHandler
HandlerClass = Handler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"
HandlerClass.protocol_version = Protocol
server_address = ('192.168.79.103', 8000)
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."

#start the server
httpd.serve_forever()

"""
