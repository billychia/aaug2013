#!/usr/bin/python
'''minmal AMI client'''

import socket

#create an socket
sock = socket.socket()
#now connect to manager on default port 5038
sock.connect(("localhost", 5038))

#send auth creds to login
sock.send("action: login\r\n")
sock.send("username: user\r\n")
sock.send("secret: password\r\n\r\n")

#receive response
line = ''
response = ''
while (line[-4:] != '\r\n\r\n'):
   line = sock.recv(1024)
   response += line

print response

#close the socket
sock.close()

