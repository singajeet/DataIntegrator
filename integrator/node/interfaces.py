"""
.. module:: integrator.node.interfaces
        :platform: Unix, Windows
        :synopsis: Abstract decleration of an node in distributed system

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
import enum
from flufl.i18n import initialize
from yapsy.IPlugin import IPlugin

_ = initialize(__file__)


class NodeNotImplementedError(Exception):
    """Exception will be raised if no implementation found for INode
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class IAbstractNode:
    """Represents an abstract node in distributed network
    """

    _node_name = None
    _node_type = None
    _node_host = None
    _node_port = None

    @property
    def node_name(self):
        return self._node_name

    @node_name.setter
    def node_name(self, value):
        self._node_name = value

    @property
    def node_type(self):
        return self._node_type

    def exists(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def create_node(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def find_master(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def declare_node_as_master(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def start_node(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def stop_node(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def node_status(self):
        NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def install_container(self, container):
        NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def uninstall_container(self, container_id):
        NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def register_container(self, container_id):
        NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def activate_container(self, container_id):
        NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def deactivate_container(self, container_id):
        NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def list_containers(self):
        NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))


class INodeType(enum.Enum):
    """Types of node supported
    """
    BASIC = 1
    ADVANCED = 2
    OTHERS = -1


class INode(IPlugin, IAbstractNode):
    """interface for the plugins implementations
    """

    _iplugin_name = None
    _iplugin_type = None

    @property
    def iplugin_name(self):
        return self._iplugin_name

    @iplugin_name.setter
    def iplugin_name(self, value):
        self._iplugin_name = value

    @property
    def iplugin_type(self):
        return self._iplugin_type

