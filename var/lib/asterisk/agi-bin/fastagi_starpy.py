#! /usr/bin/env python
"""Simple FastAGI server using starpy"""
from twisted.internet import reactor
from starpy import fastagi
import logging, time

log = logging.getLogger( 'getSay' )

def getSay( agi ):
   """Get a custom variable and speak characters with say Alpha"""
   log.debug( 'testFunction' )
   def getX():
      return agi.getVariable( 'my_custom_var' )
   def sayX( result ):
      return agi.sayAlpha( result )
   def done( result ):
      return agi.finish()
   return getX().addCallback( sayX ).addCallback( done )

if __name__ == "__main__":
   logging.basicConfig()
   fastagi.log.setLevel( logging.DEBUG )
   f = fastagi.FastAGIFactory( getSay )
   reactor.listenTCP( 4573, f, 50, '127.0.0.1' ) # only binding on local interface
   reactor.run()
