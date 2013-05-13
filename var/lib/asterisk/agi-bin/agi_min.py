#!/usr/bin/python

# Need to import sys to deal with i/o
import sys

# Loop to read variables from Asterisk
while True:
   # Read in one line from stdin
   line = sys.stdin.readline().strip()
   # Stop looping when Asterisk sends empty line
   if not line:
      break

# Send Asterisk an AGI command
sys.stdout.write('verbose "AGI is fun!" 0 \n')
# Flush the buffer so the script doesn't get stuck
sys.stdout.flush()
# Read the response from Asterisk
response = sys.stdin.readline().strip()
# Print response on stderr - use asterisk -c to view
sys.stderr.write('%s \n' % response)


