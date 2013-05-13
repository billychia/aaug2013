#! /usr/bin/env python
"""Example script to generate a call to connect a remote channel to an IVR"""
from starpy import manager
from twisted.internet import reactor
import sys, logging

channel = 'sip/adorner'
#channel = 'local/null'
context, exten, priority = 'default', 'demo', 1

def main( channel = channel, connectTo=(context, exten, priority) ):
        """1 = AMI Username 2 = Secret, use: manager_starpy.py user password"""
	f = manager.AMIFactory(sys.argv[1], sys.argv[2])
	df = f.login()
	def onLogin( protocol ):
		"""On Login, attempt to originate the call"""
		context, extension, priority = connectTo
		df = protocol.originate(
			channel,
			context,extension,priority,
		)
		def onFinished( result ):
			df = protocol.logoff()
			def onLogoff( result ):
				reactor.stop()
			return df.addCallbacks( onLogoff, onLogoff )
		def onFailure( reason ):
			print reason.getTraceback()
			return reason 
		df.addErrback( onFailure )
		df.addCallbacks( onFinished, onFinished )
		return df 
	def onFailure( reason ):
		"""Unable to log in!"""
		print reason.getTraceback()
		reactor.stop()
	df.addCallbacks( onLogin, onFailure )
	return df

if __name__ == "__main__":
	manager.log.setLevel( logging.DEBUG )
	logging.basicConfig()
	reactor.callWhenRunning( main )
	reactor.run()
