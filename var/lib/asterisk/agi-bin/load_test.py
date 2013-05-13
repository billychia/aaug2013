#!/usr/bin/python
'''small script for load testing
use: python load_test.py [exten] [num_tests]'''

import sys
from subprocess import call
from time import sleep

exten = 'fastagi'
if (len(sys.argv) == 2):
   exten = str(sys.argv[1])

num_tests = 1
if (len(sys.argv) == 3):
   num_tests = int(sys.argv[2])

cmd = "asterisk"
args = "-rx channel originate local/null@default extension {0}@default".format(exten)

for x in range(num_tests):
   call([cmd, args])

for x in range(10):
   print 'done', call(['uptime'])
   sleep(1)
