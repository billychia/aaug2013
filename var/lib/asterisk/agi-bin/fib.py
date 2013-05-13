#!/usr/bin/python

import sys

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

#create a dict to store environment variables
env = {}

#loop to read variables from Asterisk
while 1:
   # read in one line from stdin
   line = sys.stdin.readline().strip()

   # if the line is empty Asterisk is done sending 
   if line == '':
      break

   key,data = line.split(':')
   if key[:4] != 'agi_':
      #skip input that doesn't begin with agi_
      sys.stderr.write("Did not work!\n");
      sys.stderr.flush()
      continue
   key = key.strip()
   data = data.strip()
   if key != '':
      env[key] = data

sys.stdout.write("set variable var %s \n" % fib(int(env['agi_arg_1'])))
sys.stdout.flush()
