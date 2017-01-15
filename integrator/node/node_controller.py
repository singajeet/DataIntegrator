"""
.. module:: integrator.node.node_controller
        :platform: Unix, Windows
        :synopsis: Abstract decleration of an node in distributed system

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from __future__ import unicode_literals
from integrator.log.logger import create_logger
import integrator.node.interfaces as interfaces
from yapsy.PluginManager import PluginManager
import sys
from flufl.i18n import initialize


_ = initialize(__file__)
logger = create_logger(__package__)
loggeryapsy = create_logger('yapsy')

if __name__ == '__main__':
    logger.info(_('Data Integrator node has been started...'))

    logger.info(_('Initiating plug-in manager to load required plug-ins...'))
    simple_plugin_manager = PluginManager()
    logger.debug(_('Plug-in manager has been started'))
    simple_plugin_manager.setPluginPlaces(['./integrator/plugins'])
    logger.debug(_('Plugin-in manager will search for plug-ins in folder: /integrator/plugins'))
    simple_plugin_manager.locatePlugins()
    simple_plugin_manager.loadPlugins()
    # simple_plugin_manager.setCategoriesFilter({
    #                                           'Node': interfaces.INode,
    #                                           'DBCredentials': interfaces.INodeDBCredentials,
    #                                           'DatabaseManager': interfaces.INodeDatabaseManager
    #                                           })
    # print('Node Plugins: ')
    # for plugins in simple_plugin_manager.getPluginsOfCategory('Node'):
    #     print plugins.name
    # print('DB Credentials Plugins: ')
    # for plugins in simple_plugin_manager.getPluginsOfCategory('DBCredentials'):
    #     print plugins.name
    # print('Database Manager Plugins: ')
    # for plugins in simple_plugin_manager.getPluginsOfCategory('DatabaseManager'):
    #     print plugins.name
    for plugins in simple_plugin_manager.getAllPlugins():
        print plugins.name
    # node = INode()
    # node.load_system_details()
    # logger.debug(_('System details loaded'))
    # logger.debug(node.node_details)

    # v_sys_id = node.sys_id_exists()
    # if v_sys_id == -1:
    #     logger.info(_('No existing sys id found'))
    #     v_sys_id = node.create_node()
    #     logger.debug(_('sys id saved for this node'))

    # if not node.validate_sys_id(v_sys_id):
    #     logger.error(_('Integrity check failed! System will exit now'))
    #     sys.exit(1)

    # db_cred = INodeDBCredentials()
    # (user, password) = (None, None)
    # if not db_cred.credentials_exists():
    #     logger.debug(_('No db credentials found, user will be prompted for same'))
    #     (user, password) = db_cred.prompt_credentials()
    #     logger.debug(_('New db credentials: %s | %s') % (user, password))
    #     db_cred.save_credentials()
    #     logger.debug(_('db credentials saved successfully'))
    # else:
    #     logger.debug(_('db credentials found and will be loaded'))
    #     db_cred.load_credentials()
    #     (user, password) = db_cred.get_credentials()
    #     logger.debug(_('Credentials loaded successfully: %s %s') % (user, password))

    # db_manager = INodeDatabaseManager(user, password)
    # logger.info(_('Node\'s database manager has been started'))
    # if not db_manager.node_db_exists():
    #     logger.debug(_('Database is not configured yet and will be initiated now'))
    # else:
    #     logger.debug(_('Node database found and will be initialized'))
    # db_manager.open_or_create_database()

    # if not db_manager.node_details_exists(v_sys_id):
    #     db_manager.save_node_details(node.get_node_details())
    # else:
    #     db_manager.load_node_details(v_sys_id)

    # logger.debug(_('Database configured successfully!'))
