#!/usr/bin/env python
from twisted.internet import protocol,reactor
from twisted.protocols import ident
import config
import qwebirc.config_options as config_options

DEFAULT_USER = 'nobody'

# Global user <-> port map.
user_dict = {}

class IdentProtocol(ident.IdentServer):
        """
        Extension of the Twisted twisted.protocols.ident.IdentServer
        class to provide ident responses for users logged in to qwebirc.
        """
        def lookup(self,serverAddress,clientAddress):
                """
                Handle an actual ident response. Find out which user is on the port
                specified by serverAddress[1] and return their name.
                """
                print "Received lookup for %s -> %s" % (serverAddress,clientAddress)
                
                for (portnum,user) in user_dict.iteritems():
                        if serverAddress[1] == portnum:
                                return (config.IDENTD_OS,user.__str__())
                print user_dict
                
                return (config.IDENTD_OS,DEFAULT_USER)

class IdentFactory(protocol.ServerFactory):
        protocol = IdentProtocol

if __name__ == '__main__':
        reactor.listenTCP(1113,IdentFactory())
        reactor.run()
