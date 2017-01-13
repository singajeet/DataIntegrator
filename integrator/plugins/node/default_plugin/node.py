"""
.. module:: integrator.node.plug
        :platform: Unix, Windows
        :synopsis: Abstract decleration of an node in distributed system

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from integrator.node.interfaces import INode, INodeType, INodeInfo
from flufl.i18n import initialize
from Crypto.Hash import SHA256
import logging
import platform
import uuid
import socket
import os
import sys

_ = initialize(__file__)


class NodeInfo(INodeInfo):
    """
    """

    def __init__(self):
        self._machine = platform.machine()
        self._node = platform.node()
        self._platform = platform.platform()
        self._processor = platform.processor()
        self._release = platform.release()
        self._system = platform.system()
        self._version = platform.version()

    def get_hash(self):
        self._mac_address = uuid.getnode()
        self._sys_identifier = SHA256.new(self._mac_address).hexdigest()

    def __str__(self):
        return """Machine: %s
                    Node: %s
                    Platform: %s
                    Processor: %s
                    Release: %s
                    System: %s
                    Version: %s
                """.format(self._machine, self._node,
                           self._platform, self._processor,
                           self._release, self._system, self._version)


class Node(INode):
    """Implementation of the INode interface
    """

    _node_type = INodeType.BASIC
    _logger = logging.getLogger('%s.INode' % __package__)
    _kwds = None
    _sys_id_file_name = 'sys.node.id.hash'
    _db_file_name = 'db.node.json'

    def load_system_details(self):
        self._system_details = NodeInfo()
        self._node_name = self._system_details._node
        self._node_host = socket.gethostbyname(socket.gethostname())
        self._node_port = 1344

    def get_node_info(self):
        return self._system_details

    def hash_exists(self):
        if os.path.isfile(self._sys_id_file_name):
            try:
                with open(self._sys_id_file_name, 'r') as hfile:
                    v_sys_id = hfile.read()
            except IOError as e:
                self._logger.error(_('Unable to open sys identifier file. Could be an permission isuue: %s') % (e.message))
                sys.exit(-1)

            if v_sys_id != self._system_details.get_hash():
                self._logger.error(_('WARNING! Tampered sys identifier file for this node. System will exit!'))
                sys.exit(-1)

            return True
        else:
            return False

    def create_node(self):
        try:
            self._logger.debug(_('User choosed to configure a new node on this machine'))
            with open(self._sys_id_file_name, 'w') as hfile:
                hfile.write(self._system_details.get_hash())
                self._logger.debug(_('New sys id file created for this node and saved!'))
        except IOError as e:
            self._logger.error(_('Unable to create new sys id file. System will exit: %s') % (e.message))
            sys.exit(-1)

    def __init__(self):
        """ Default constructor of an node
        """
        self.load_system_details()
        self._logger.info('Node has been initialized')













