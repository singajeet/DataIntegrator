"""
.. module:: integrator.node.node_controller
        :platform: Unix, Windows
        :synopsis: Abstract decleration of an node in distributed system

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""

# Required modules are imported below
from __future__ import unicode_literals
from integrator.log.logger import create_logger
from flufl.i18n import initialize
from config import Config
from constantly import ValueConstant, Values
from yapsy.PluginManager import PluginManager
import importlib


# Define constants
class constants(Values):
    CONFIG_FILE = ValueConstant('node.ini')


# Initialize internationalization for the node
_ = initialize(__file__)
logger = create_logger(__name__)
config = Config(constants.CONFIG_FILE.value)


class plugin_types(Values):
    NODE_PLUGIN = ValueConstant(config.node_plugin)
    AUTH_PROVIDER_PLUGIN = ValueConstant(config.auth_provider_plugin)
    NODE_DB_PLUGIN = ValueConstant(config.node_db_plugin)
    NETWORK_SERVICE = ValueConstant(config.network_service_plugin)


def load_class(full_class_string):
    """
    dynamically load a class from a string
    """

    class_data = full_class_string.split(".")
    module_path = ".".join(class_data[:-1])
    class_str = class_data[-1]

    module = importlib.import_module(module_path)
    # Finally, we retrieve the Class
    return getattr(module, class_str)


class PluginLoader:

    _filters = dict()
    _manager = None
    _plugin_path = config.plugin_path

    def __init__(self, config_section=config.plugin_filters):
        self.load_filters_from_config(config_section)
        self.init_plugin_manager()

    def add_filter(self, filter_name, filter_type):
        """
        """
        logger.debug('New filter added: %s' % filter_name)
        self._filters.update({filter_name: filter_type})

    def remove_filter(self, filter_name):
        """
        """
        logger.debug('Filter deleted: %s' % filter_name)
        del self._filter[filter_name]

    def load_filters_from_config(self, config_section):
        logger.debug('Loading filters from config section: %s' % config_section)
        for conf_filter in config_section:
            self.add_filter(conf_filter.category, load_class(conf_filter.type))

    def init_plugin_manager(self):
        logger.debug('PluginManager initiated with categories: %s' % self._filters)
        self._manager = PluginManager(categories_filter=self._filters)
        logger.debug('Searching plugins in folder: %s' % self._plugin_path)
        self._manager.setPluginPlaces([self._plugin_path])
        self._manager.collectPlugins()

    def list_all_plugins(self):
        for plug in self._manager.getAllPlugins():
            print('Plugin Name: %s' % plug.name)
            logger.debug('Plugin Name: %s' % plug.name)

    def get_node_plugin(self):
        return self._manager.getPluginByName(plugin_types.NODE_PLUGIN.value, category='Node').plugin_object

    def get_auth_plugin(self):
        return self._manager.getPluginByName(plugin_types.AUTH_PROVIDER_PLUGIN.value, category='AuthProvider').plugin_object

    def get_db_plugin(self):
        return self._manager.getPluginByName(plugin_types.NODE_DB_PLUGIN.value, category='DatabaseManager').plugin_object

    def get_broadcast_plugin(self):
        return self._manager.getPluginByName(plugin_types.NETWORK_SERVICE.value, category='NetworkService').plugin_object


# if __name__ == '__main__':
#     ploader = PluginLoader()
#     ploader.list_all_plugins()

#     print(ploader.get_node_plugin())
#     print(ploader.get_auth_plugin())
#     print(ploader.get_db_plugin())
#     print(ploader.get_broadcast_plugin())
