#!/usr/bin/python

# Import Pyst Asterisk AGI module
import sys
import asterisk.agi

# Takes care of reading in variables
agi = asterisk.agi.AGI()
# Get a channel variable from Asterisk
my_custom_var = agi.get_variable('my_custom_var')
# Wrapper for the 'SAY ALPHA' agi commmand, strip extra quotes 
agi.say_alpha(my_custom_var[1:-1])
# Hangup the channel
agi.hangup()
# Exit the python interpreter
sys.exit(0)

