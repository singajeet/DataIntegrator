"""
.. module:: integrator.node.plug
        :platform: Unix, Windows
        :synopsis: Abstract decleration of an network objects in distributed system

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from yapsy.IPlugin import IPlugin
from twisted.internet.protocol import DatagramProtocol, Protocol, Factory
from twisted.application import service


class INetwork(IPlugin):
    """
    """


class INetworkHost(IPlugin):
    """
    """


class INetworkPort(IPlugin):
    """
    """

# ####################################################################################


class INetworkProtocol(INetwork):
    """
    """


class INetworkDatagramProtocol(INetworkProtocol, DatagramProtocol):
    """An subclass of twisted DatagramProtocol class
        All below attributes and methods should be
        implemented by base class
    """
    factory = None

    def __init__(self):
        DatagramProtocol.__init__(self)

    def startProtocol(self):
        pass

    def datagramReceived(self, datagram, ip_address):
        pass

    def connectionRefused(self):
        pass


class INetworkTCProtocol(INetworkProtocol, Protocol):
    """An subclass of twisted Protocol class
        All below attributes and methods should be
        implemented by base class
    """
    factory = None

    def __init__(self):
        Protocol.__init__(self)

    def connectionMade(self):
        pass

    def connectionLost(self, reason):
        pass

    def dataReceived(self, data):
        pass


# ######################################################################################


class INetworkFactory(IPlugin, Factory):
    """An subclass of twisted Factory class
        All below attributes and methods should be
        implemented by base class
    """
    protocol = None

    def __init__(self):
        Factory.__init__(self)

    def startFactory(self):
        pass

    def stopFactory(self):
        pass

    def buildProtocol(self, ip_address):
        pass


class INetworkTask(INetwork):
    """
    """


class INetworkService(IPlugin, service.Service):
    """Service is used to create Factory instance
    and compose Protocol + any custom functionality
    into Factory. Service will have getter's of
    factory defined.
    """
    # define custom functions as shown in below example
    # def getUser(self):
    #   return someUser
    #
    # define factory getter as shown below
    # def getXYZFactory(self):
    #   f = INetworkFactory()  -------> should be an instance of derived class to this interface
    #   f.protocol = INetworkProtocol ---------> Reference to derived class of INetworkProtocol
    #   f.getUser = self.getUser ----------> Reference to custom functions defined in Service
    #   return f

    def __init__(self):
        service.Service.__init__(self)

    def startService(self):
        pass

    def stopService(self):
        pass







