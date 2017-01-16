"""
.. module:: integrator.node.node_controller
        :platform: Unix, Windows
        :synopsis: Abstract decleration of an node in distributed system

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""

# Required modules are imported below
from __future__ import unicode_literals
from integrator.log.logger import create_logger
import integrator.node.interfaces as interfaces
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
    DB_AUTH_PROVIDER_PLUGIN = ValueConstant(config.db_auth_provider_plugin)
    NODE_DB_PLUGIN = ValueConstant(config.node_db_plugin)


# Main entry point of the node program
if __name__ == '__main__':
    logger.info(_('Data Integrator node has been started...'))

    # ####################### Initiate plugin manager ################################################
    logger.info(_('Initiating plug-in manager to load required plug-ins...'))
    plugin_manager = PluginManager(categories_filter={'Node': interfaces.INode,
                                                      'DBAuthProvider': interfaces.INodeDBAuthProvider,
                                                      'DatabaseManager': interfaces.INodeDatabaseManager
                                                      })
    logger.debug(_('Plug-in manager has been started'))
    plugin_manager.setPluginPlaces([config.plugin_path])
    logger.debug(_('Plugin-in manager will search for plug-ins in folder: /integrator/plugins'))
    plugin_manager.collectPlugins()

    # ####################### Filter out the plugins required in this program ##########################
    node = plugin_manager.getPluginByName(constants.NODE_PLUGIN.value, category='Node').plugin_object
    db_cred = plugin_manager.getPluginByName(constants.DB_AUTH_PROVIDER_PLUGIN.value, category='DBAuthProvider').plugin_object
    db_manager = plugin_manager.getPluginByName(constants.NODE_DB_PLUGIN.value, category='DatabaseManager').plugin_object

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

    (user, password) = (None, None)
    if not db_cred.credentials_exists():
        logger.debug(_('No db credentials found, user will be prompted for same'))
        (user, password) = db_cred.prompt_credentials()
        logger.debug(_('New db credentials: %s | %s') % (user, password))
        db_cred.save_credentials()
        logger.debug(_('db credentials saved successfully'))
    else:
        logger.debug(_('db credentials found and will be loaded'))
        db_cred.load_credentials()
        (user, password) = db_cred.get_credentials()
        logger.debug(_('Credentials loaded successfully: %s %s') % (user, password))

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
