"""
.. module:: integrator.node.interfaces
        :platform: Unix, Windows
        :synopsis: Abstract decleration of an node in distributed system

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from flufl.i18n import initialize
from yapsy.IPlugin import IPlugin
from constantly import NamedConstant, Names

_ = initialize(__file__)


class NodeNotImplementedError(Exception):
    """Exception will be raised if no implementation found for INode
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class INodeInfo:
    """A node representation and its attributes as abstract class
    """
    _machine = None
    _node = None
    _platform = None
    _processor = None
    _release = None
    _system = None
    _version = None
    _mac_address = None
    _sys_identifier = None

    def get_hash(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))


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

    def get_node_info(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def _load_system_details(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def _exists(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def _create_node(self):
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


class INodeType(Names):
    """Types of node supported
    """
    BASIC = NamedConstant()
    ADVANCED = NamedConstant()
    OTHERS = NamedConstant()


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


class INodeDatabaseType(Names):
    """
    """
    TINYDB = NamedConstant()
    SQLITE = NamedConstant()
    SQLITE_INMEMORY = NamedConstant()
    ORACLE = NamedConstant()
    MYSQL = NamedConstant()
    MSSQL = NamedConstant()


class NodeDatabaseNotImplementedError:
    """
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class INodeDatabase(IPlugin):
    """
    """

    _database_name = None
    _database_type = None
    _iplugin_name = None
    _iplugin_type = None

    def _load_db_details(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def _exists(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def _create_database(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def load_node_details(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def save_node_details(self, node):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))


class INodeDBCredentials(IPlugin):
    """
    """
    _user_name = None
    _password = None
    _iplugin_name = None
    _iplugin_type = None

    def __init__(self, file_name):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def credentials_exists(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def prompt_credentials(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def save_credentials(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def load_credentials(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def get_credentials(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))















