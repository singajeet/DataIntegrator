"""
.. module:: integrator.node.plug
        :platform: Unix, Windows
        :synopsis: Abstract decleration of an node in distributed system

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from integrator.node.interfaces import INode, INodeType
from flufl.i18n import initialize
from Crypto.Hash import SHA256
from prompt_toolkit.shortcuts import confirm
import logging
import platform
import uuid
import socket
import os
import sys

_ = initialize(__file__)


class nsystem:
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
        self._system_hash = SHA256.new(self._mac_address).hexdigest()

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
    _hash_file_name = '.node.hash'

    def _load_system_details(self):
        self._system_details = nsystem()
        self._node_name = self._system_details._node
        self._node_host = socket.gethostbyname(socket.gethostname())
        self._node_port = 1344

    def exists(self):
        if os.path.isfile(self._hash_file_name):
            try:
                with open(self._hash_file_name, 'r') as hfile:
                    v_hash = hfile.read()
            except IOError as e:
                self._logger.error(_('Unable to open hash file. Could be an permission isuue: %s') % (e.message))
                sys.exit(-1)

            if v_hash != self._system_details.get_hash():
                self._logger.error(_('WARNING! Tampered hash file for this node. System will exit!'))
                sys.exit(-1)

            return True
        else:
            return False

    def create_node(self):
        try:
            self._logger.debug(_('User choosed to configure a new node on this machine'))
            with open(self._hash_file_name, 'w') as hfile:
                hfile.write(self._system_details.get_hash())
                self._logger.debug(_('New hash file created for this node and saved!'))
        except IOError as e:
            self._logger.error(_('Unable to create new hash file. System will exit: %s') % (e.message))
            sys.exit(-1)

    def __init__(self):
        """ The node information will be initialized in the constructor.
            IP address and Port will be assigned to be used for this node
            and hash will be prepared to validate the database information
            for this node
        """
        self._logger.info('Node has been initialized')
        self._load_system_details()
        if self.exists():
                self._looger.debug(_('Found an existing node and same will be booted'))
        else:
            self._logger.info(_('No previous intallation found on this node'))
            response = confirm(message=_('A new node will be configiured. Proceed(Y/N): '))

            if response:
                self.create_node()
            else:
                self._logger.info(_('Configuration terminated as per the selection'))












