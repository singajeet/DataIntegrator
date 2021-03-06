"""
.. module:: integrator.node.interfaces
        :platform: Unix, Windows
        :synopsis: Abstract decleration of an node in distributed system

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from flufl.i18n import initialize
from yapsy.IPlugin import IPlugin
from constantly import NamedConstant, Names, ValueConstant, Values
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from twisted.internet.selectreactor import SelectReactor


Base = declarative_base()
_ = initialize(__file__)


# ########################### Constants defined below #################################3
class NodeRole(Names):
    """
    """
    MASTER = NamedConstant()
    SLAVE = NamedConstant()
    BACKUP = NamedConstant()


class AuthProviderType(Values):
    """
    """
    GENERIC = ValueConstant('DI_GENERIC')
    NODE = ValueConstant('DI_NODE')
    NODE_DB = ValueConstant('DI_NODE_DB')
    CONTAINER = ValueConstant('DI_CONTAINER')
    SERVICE = ValueConstant('DI_SERVICE')


class INodeType(Names):
    """Types of node supported
    """
    BASIC = NamedConstant()
    ADVANCED = NamedConstant()
    OTHERS = NamedConstant()


class INodeDatabaseType(Names):
    """
    """
    TINYDB = NamedConstant()
    SQLITE = NamedConstant()
    SQLITE_INMEMORY = NamedConstant()
    ORACLE = NamedConstant()
    MYSQL = NamedConstant()
    MSSQL = NamedConstant()


# ################################# Custom Exception Defined ####################################
class NodeNotImplementedError(Exception):
    """Exception will be raised if no implementation found for INode
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class NodeDatabaseNotImplementedError(Exception):
    """
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class NodeDBAuthProviderNotImplementedError(Exception):
    """
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


# ####################### The model interface of Node to be used with Database ####################
class INodeModel(Base):
    """A node representation and its attributes as abstract class
    """
    __tablename__ = 'node'

    id = Column(Integer, primary_key=True)
    machine = Column(String(100))
    node = Column(String(100))
    platform = Column(String(100))
    processor = Column(String(100))
    release = Column(String(100))
    system = Column(String(100))
    version = Column(String(100))
    mac_address = Column(String(100))
    sys_identifier = Column(String(100))
    node_name = Column(String(100))
    node_host = Column(String(100))
    node_port = Column(Integer)
    node_role = Column(String(100))
    modified_on = Column(DateTime, default=datetime.utcnow)

    def get_sys_id_hash(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))


# ########################## An abstract definition of Node #########################################
class IAbstractNode:
    """Represents an abstract node in distributed network
    """
    _node_type = None

    @property
    def node_type(self):
        return self._node_type

    def get_node_details(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def load_system_details(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def sys_id_exists(self):
        raise NodeNotImplementedError(_('Node member not implemented'), _('This functionality is not available as no implementation found'))

    def validate_sys_id(self, v_sys_id):
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


# ############### An abstract interface of Node as plugin and reactor all services##################
class INode(IPlugin, IAbstractNode, SelectReactor):
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


# ################### An interface to manager database objects related to Node ###################
class INodeDatabaseManager(IPlugin):
    """
    """

    _database_name = None
    _database_type = None
    _iplugin_name = None
    _iplugin_type = None

    def prepare_node_session(self, dbcredentials):
        raise NodeDatabaseNotImplementedError(_('Node member not implemented'), _(
            'This functionality is not available as no implementation found'))

    def node_db_exists(self):
        raise NodeDatabaseNotImplementedError(_('Node member not implemented'), _(
            'This functionality is not available as no implementation found'))

    def validate_database(self):
        raise NodeDatabaseNotImplementedError(_('Node member not implemented'), _(
            'This functionality is not available as no implementation found'))

    def open_or_create_database(self):
        raise NodeDatabaseNotImplementedError(_('Node member not implemented'), _(
            'This functionality is not available as no implementation found'))

    def load_node_details(self, sys_id):
        raise NodeDatabaseNotImplementedError(_('Node member not implemented'), _(
            'This functionality is not available as no implementation found'))

    def save_node_details(self, node):
        raise NodeDatabaseNotImplementedError(_('Node member not implemented'), _(
            'This functionality is not available as no implementation found'))

    def node_details_exists(self, sys_id):
        raise NodeDatabaseNotImplementedError(_('Node member not implemented'), _(
            'This functionality is not available as no implementation found'))

    def update_node_details(self, node):
        raise NodeDatabaseNotImplementedError(_('Node member not implemented'), _(
            'This functionality is not available as no implementation found'))


# ################ An abstract interface to Auth provider to be used by DB Manager #############
class INodeAuthProvider(IPlugin):
    """
    """
    _user_name = None
    _password = None
    _iplugin_name = None
    _iplugin_type = None
    _type = None

    def __init__(self, file_name):
        raise NodeDBAuthProviderNotImplementedError(_('Node member not implemented'), _(
            'This functionality is not available as no implementation found'))

    def set_type(self, auth_type):
        raise NodeDBAuthProviderNotImplementedError(_('Node member not implemented'), _(
            'This functionality is not available as no implementation found'))

    def credentials_exists(self):
        raise NodeDBAuthProviderNotImplementedError(_('Node member not implemented'), _(
            'This functionality is not available as no implementation found'))

    def prompt_credentials(self):
        raise NodeDBAuthProviderNotImplementedError(_('Node member not implemented'), _(
            'This functionality is not available as no implementation found'))

    def save_credentials(self):
        raise NodeDBAuthProviderNotImplementedError(_('Node member not implemented'), _(
            'This functionality is not available as no implementation found'))

    def load_credentials(self):
        raise NodeDBAuthProviderNotImplementedError(_('Node member not implemented'), _(
            'This functionality is not available as no implementation found'))

    def get_credentials(self):
        raise NodeDBAuthProviderNotImplementedError(_('Node member not implemented'), _(
            'This functionality is not available as no implementation found'))
