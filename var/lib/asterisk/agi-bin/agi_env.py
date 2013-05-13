#!/usr/bin/python
'''AGI script that shows reading env variables
and accessing them from the dictionary'''

# Need to import sys to deal with i/o
import sys
# Import pretty print to print dictionary
import pprint

# Create a dict to store AGI variables from Asterisk
env = {}

# Loop to read variables from Asterisk
while True:
   # Read in one line from stdin
   line = sys.stdin.readline().strip()
   # Stop looping when Asterisk sends empty line
   if not line:
      break
   # Add lines as key/value pair to env
   key,value = line.split(':')
   key = key.strip()
   value = value.strip()
   if key:
      env[key] = value
# Show env dictionary on stderr - use asterisk -c to view
sys.stderr.write(pprint.pformat(env))
sys.stderr.write('\n')

# Access arg1 variable from env 
sys.stdout.write('verbose %s 0 \n' % env['agi_arg_1'])
# Flush the buffer so the script doesn't get stuck
sys.stdout.flush()
# Read the response from Asterisk
response = sys.stdin.readline().strip()
# Print response on stderr - use asterisk -c to view
sys.stderr.write('%s \n' % response)


