"""
.. module:: integrator.node.node_controller
        :platform: Unix, Windows
        :synopsis: Abstract decleration of an node in distributed system

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""

# Required modules are imported below
from __future__ import unicode_literals
from integrator.log.logger import create_logger
import integrator.core.interfaces.node as node_interface
import integrator.core.interfaces.network as network_interface
from yapsy.PluginManager import PluginManager
import sys
from flufl.i18n import initialize
from config import Config
from constantly import ValueConstant, Values


# Initialize internationalization for the node
_ = initialize(__file__)

# Initialize loggers for node and yapsy plugin manager
logger = create_logger(__package__)
loggeryapsy = create_logger('yapsy')

# Initialize configuration for the node
confile = file('node.ini')
config = Config(confile)


# Constants to be used in this program
class constants(Values):
    NODE_PLUGIN = ValueConstant(config.node_plugin)
    AUTH_PROVIDER_PLUGIN = ValueConstant(config.auth_provider_plugin)
    NODE_DB_PLUGIN = ValueConstant(config.node_db_plugin)
    NETWORK_SERVICE = ValueConstant(config.network_service_plugin)


# Main entry point of the node program
if __name__ == '__main__':
    logger.info(_('Data Integrator node has been started...'))

    # ####################### Initiate plugin manager ################################################
    logger.info(_('Initiating plug-in manager to load required plug-ins...'))
    plugin_manager = PluginManager(categories_filter={'Node': node_interface.INode,
                                                      'AuthProvider': node_interface.INodeAuthProvider,
                                                      'DatabaseManager': node_interface.INodeDatabaseManager,
                                                      'NetworkService': network_interface.INetworkService
                                                      })
    logger.debug(_('Plug-in manager has been started'))
    plugin_manager.setPluginPlaces([config.plugin_path])
    logger.debug(_('Plugin-in manager will search for plug-ins in folder: /integrator/plugins'))
    plugin_manager.collectPlugins()

    # ####################### Filter out the plugins required in this program ##########################
    node = plugin_manager.getPluginByName(constants.NODE_PLUGIN.value, category='Node').plugin_object
    if node is None:
        logger.error(_('No plugin available with Node functionality, system will exit now'))
        sys.exit(1)

    db_auth = plugin_manager.getPluginByName(constants.AUTH_PROVIDER_PLUGIN.value, category='AuthProvider').plugin_object
    if db_auth is None:
        logger.error(_('No plugin available with Auth functionality, system will exit now'))
        sys.exit(1)

    db_manager = plugin_manager.getPluginByName(constants.NODE_DB_PLUGIN.value, category='DatabaseManager').plugin_object
    if db_manager is None:
        logger.error(_('No plugin available with DB Manager functionality, system will exit now'))
        sys.exit(1)

    broadcaster = plugin_manager.getPluginByName(constants.NETWORK_SERVICE.value, category='NetworkService').plugin_object
    if broadcaster is None:
        logger.error(_('No plugin available with Broadcaster functionality, system will exit now'))
        sys.exit(1)
    # ####################### Load the system details to be used by Node ###############################
    node.load_system_details()
    logger.debug(_('System details loaded'))
    logger.debug(node.node_details)

    v_sys_id = node.sys_id_exists()
    if v_sys_id == -1:
        logger.info(_('No existing sys id found'))
        v_sys_id = node.create_node()
        logger.debug(_('sys id saved for this node'))

    if not node.validate_sys_id(v_sys_id):
        logger.error(_('Integrity check failed! System will exit now'))
        sys.exit(1)

    # ############### Setup auth provider for accessing Node database #################################
    (user, password) = (None, None)
    db_auth.set_type(auth_type=node_interface.AuthProviderType.NODE_DB)
    if not db_auth.credentials_exists():
        logger.debug(_('No db credentials found, user will be prompted for same'))
        (user, password) = db_auth.prompt_credentials()
        logger.debug(_('New db credentials: %s | %s') % (user, password))
        db_auth.save_credentials()
        logger.debug(_('db credentials saved successfully'))
    else:
        logger.debug(_('db credentials found and will be loaded'))
        db_auth.load_credentials()
        (user, password) = db_auth.get_credentials()
        logger.debug(_('Credentials loaded successfully: %s %s') % (user, password))

    # ########################### Initiate Node's database manager ###################################
    logger.info(_('Node\'s database manager has been started'))
    if not db_manager.node_db_exists():
        logger.debug(_('Database is not configured yet and will be initiated now'))
    else:
        logger.debug(_('Node database found and will be initialized'))
    db_manager.open_or_create_database()

    if not db_manager.node_details_exists(v_sys_id):
        db_manager.save_node_details(node.get_node_details())
    else:
        db_manager.load_node_details(v_sys_id)

    logger.debug(_('Database configured successfully!'))

    # ########################## Start broadcaster to check for master node ##########################
    node.find_master(broadcaster)
