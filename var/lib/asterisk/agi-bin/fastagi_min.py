#! /usr/bin/env python

import socket

#create an socket
sock = socket.socket()
#bind to default agi 4573
sock.bind(("localhost", 4573))
#listen for connections
sock.listen(1)

while True:
   #accept connections on the socket
   connection, remoteSock = sock.accept()
   print 'Opened connection with ', remoteSock
   while True:
      # Read in one line from the connection
      line = connection.recv(1024).strip()
      print line
      # Stop looping when Asterisk sends empty line
      if not line:
	 break
   connection.send('verbose "fastAGI is fun!" 0 \n')
   response = connection.recv(1024).strip()
   print response
   connection.close()

