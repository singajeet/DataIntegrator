from integrator.core.interfaces.network import INetworkDatagramProtocol
from twisted.internet import reactor
from crochet import wait_for, run_in_reactor, setup
from flufl.i18n import initialize
from integrator.log.logger import create_logger


setup()
_ = initialize(__file__)


class NodeBroadcaster(INetworkFactory):
    _broadcast_address = '<broadcast>'
    _broadcast_port = 9999
    _from_ip_address = 'localhost'
    _received_message = None
    _master_found = False
    _master_ip_address = None
    _broadcast_protocol = None

    def __init__(self, from_ip='localhost', broadcast_port=9999):
        """
        """
        self.logger = create_logger('%s.INode' % (__name__))
        self._from_ip_address = from_ip
        self._broadcast_port = broadcast_port
        self.logger.debug('Node broadcaster service has been started')

    def buildProtocol(self, ip_address):
        self._protocol = NodeBroadcasterProtocol('127.0.0.1', 9999)
        return self._protocol

    def sendMessage(self, message):
        self._protocol.send_message(message)
    # @run_in_reactor
    # def start_broadcaster(self):
    #     """
    #     """
    #     self.logger.debug('Starting up the broadcast protocol')
    #     reactor.listenUDP(self._broadcast_port, self._broadcast_protocol)
    #     reactor.run()
    #     self.logger.debug('Broadcast protocol is running and waiting for incoming mesages')

    # def broadcast(self, message):
    #     """
    #     """
    #     self._broadcast_protocol.send_message(message)
    #     self.logger.debug('Message broadcasted to all nodes on the network: %s' % message)

    # @wait_for(timeout=60)
    # def get_master_address(self):
    #     address = self._broadcast_protocol.status()
    #     self.logger.debug('Find master operation result: %s' % address)
    #     return address

    # @run_in_reactor
    # def shutdown_broadcaster(self):
    #     reactor.stop()
    #     self.logger.debug('Broadcaster shutdown completed successfully')

class NodeBroadcasterProtocol(INetworkDatagramProtocol):

    _recv_message = None
    _master_address = None
    _ip_address = '127.0.0.1'
    _port = 9999

    def __initi__(self, host, port):
        """
        """
        self._port = port
        self._ip_address = host
        INetworkDatagramProtocol.__init__(self)

    def startProtocol(self):
        self.transport.setBroadcastAllowed(True)
        message = 'NEW_NODE:%s:%s' % ('127.0.0.1', 9999)
        self.transport.write(message, ('<broadcast>', 9999))

    def send_message(self, message):
        """
        """
        self.transport.write(message, ('<broadcast>', 9999))
        print('Message Broadcasted: %s' % message)

    def datagramReceived(self, datagram, address):
        self._recv_message = datagram
        print('Message Received: %s' % datagram)
        if self._recv_message.startswith('MASTER'):
            self._master_address = 'MASTER_EXIST@%s@%s' % (datagram, address)

    def status(self):
        """
        """
        return self._master_address
