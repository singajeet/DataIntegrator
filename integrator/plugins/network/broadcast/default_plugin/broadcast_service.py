from integrator.core.interfaces.network import INetworkService
from flufl.i18n import initialize
from twisted.logger import Logger
from twisted.internet.protocol import DatagramProtocol
import socket


_ = initialize(__file__)


class NodeBroadcasterService(INetworkService):
    _protocol = None

    def __init__(self):
        self.logger = Logger(namespace='NodeBroadcasterService')
        self.logger.debug('Node broadcaster services has been created')

    def getNodeBroadcastProtocol(self):
        self._protocol = NodeBroadcasterProtocol()
        return self._protocol


class NodeBroadcasterProtocol(DatagramProtocol):

    _recv_message = None
    _master_address = None
    _localhost_address = socket.gethostbyname('localhost')
    _port = 9999
    logger = Logger(namespace='NodeBroadcasterProtocol')

    def __initi__(self, port=9999):
        """
        """
        self._port = port
        self.logger.debug('Broadcast protocol has been built')
        INetworkDatagramProtocol.__init__(self)

    def startProtocol(self):
        self.transport.setBroadcastAllowed(True)
        self.logger.debug('Broadcaster protocol has been started')

    def notify_new_node_up(self):
        message = 'NEW_NODE:%s' % self._localhost_address
        self.transport.write(message, ('<broadcast>', self._port))
        self.logger.debug('Notification broadcasted for addition of new node')

    def send_message(self, message):
        """
        """
        self.transport.write(message, ('<broadcast>', self._port))
        self.logger.debug('Message Broadcasted: %s' % message)

    def datagramReceived(self, datagram, address):
        self._recv_message = datagram
        print('Message Received: %s from: %s' % (datagram, address))
        self.logger.debug('Message Received: %s from server: %s' % (datagram, address))

        if self._recv_message.startswith('MASTER'):
            self.logger.debug('Master node found @ %s with message: %s' % (address, datagram))
            self._master_address = 'MASTER_EXIST@%s@%s' % (datagram, address)

    def get_master_address(self):
        """
        """
        return self._master_address

    def get_message(self):
        return self._recv_message
