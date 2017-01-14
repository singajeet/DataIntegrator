"""
.. module:: integrator.node.plug
        :platform: Unix, Windows
        :synopsis: Abstract decleration of an node in distributed system

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from integrator.log.logger import create_logger
from integrator.node.interfaces import INode, INodeType, INodeModel, NodeRole
from flufl.i18n import initialize
import socket
import os
import sys
import platform
import uuid
from Crypto.Hash import SHA256


_ = initialize(__file__)


class NodeModel(INodeModel):
    """
    """

    def get_sys_id_hash(self):
        return self.sys_identifier

    def __str__(self):
        return ("""Machine: {}
                    Node: {}
                    Platform: {}
                    Processor: {}
                    Release: {}
                    System: {}
                    Version: {}
                """.format(self.machine, self.node,
                           self.platform, self.processor,
                           self.release, self.system, self.version))


class Node(INode):
    """Implementation of the INode interface
    """

    _iplugin_name = 'Node'
    _iplugin_type = 'NodePlugin'
    _node_type = INodeType.BASIC
    _kwds = None
    _sys_id_file_path = ('%s%s.data_integrator%s' % (os.path.expanduser('~'), os.sep, os.sep))
    _sys_id_file_name = 'sys.node.id.hash'

    def populate_node_model(self, node):
        node.machine = platform.machine()
        node.node = platform.node()
        node.platform = platform.platform()
        node.processor = platform.processor()
        node.release = platform.release()
        node.system = platform.system()
        node.version = platform.version()
        node.mac_address = uuid.getnode()
        node.sys_identifier = SHA256.new(str(node.mac_address)).hexdigest()
        node.node_name = platform.node()
        node.node_host = socket.gethostbyname(socket.gethostname())
        node.node_port = 1344
        node.role = NodeRole.MASTER

    def load_system_details(self):
        self.node_details = NodeModel()
        self.populate_node_model(self.node_details)

    def get_node_details(self):
        return self.node_details

    def sys_id_exists(self):
        self.logger.debug(_('Searching sys id at: %s') % self._sys_id_file_path)
        if os.path.isfile(('%s%s' % (self._sys_id_file_path, self._sys_id_file_name))):
            try:
                with open(('%s%s' % (self._sys_id_file_path, self._sys_id_file_name)), 'r') as hfile:
                    v_sys_id = hfile.read()
                    self.logger.debug('sys id found for this node: %s' % v_sys_id)
            except IOError as e:
                self.logger.error(_('Unable to open sys id file, system will exit now: %s') % (e.message))
                sys.exit(-1)
            return v_sys_id
        else:
            return -1

    def validate_sys_id(self, v_sys_id):
        self.logger.debug(_('Validating sys id: %s (from file) against: %s (system default)') %
                          (v_sys_id, self.node_details.sys_identifier))
        return v_sys_id == self.node_details.sys_identifier

    def create_node(self):
        try:
            if not os.path.isdir(self._sys_id_file_path):
                os.mkdir(self._sys_id_file_path)

            with open(('%s%s' % (self._sys_id_file_path, self._sys_id_file_name)), 'w') as hfile:
                hfile.write(self.node_details.get_sys_id_hash())
                self.logger.debug(_('New sys id generated: %s') % self.node_details.get_sys_id_hash())
                return self.node_details.get_sys_id_hash()
        except Exception as e:
            self.logger.error(_('Unable to create new sys id. System will exit now: %s') % (e.message))
            sys.exit(-1)

    def __init__(self):
        """ Default constructor of an node
        """
        self.logger = create_logger('%s.INode' % (__name__))
