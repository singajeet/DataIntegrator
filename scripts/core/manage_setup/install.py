"""
.. module:: scripts.core.manage_setup.install.py
        :platform: Unix, Windows
        :synopsis: Module to install and configure the Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from __future__ import unicode_literals
import logging
from config.config_manager import ConfigManager
from prompt_toolkit.shortcuts import confirm
from yapsy.PluginManager import PluginManager
from .iplugins.meta_database_interfaces import IMetadataDatabasePlugin


class SetupManager:
    """Setup Manager class is used to create and manage Data Integrator projects

    """

    logger = logging.getLogger('{}.SetupManager'.format(__package__))
    _config = None
    _plugin_manager = None

    def __init__(self):
        """Initializer of Project Manager

                Project **logging** & **configuration** will be initialized in this class
        """
        # self.logging.setLevel(level=logging.DEBUG)
        self.logger.info('Trying to load the configuration file...')
        self._config = ConfigManager()
        self.logger.info('Config Manager has been initiated using config file: {}'
                         .format(
                             self._config.config_file_name))
        self._plugin_manager = PluginManager(categories_filter={"MetaDBPlugins": IMetadataDatabasePlugin})
        self._plugin_manager.setPluginPlaces([self._config.get('Plugins', 'setup_manager_plugins', 0)])
        self._plugin_manager.locatePlugins()
        self._plugin_manager.loadPlugins()

    def list_db(self):
        """Provides the list of all installed plugins that can be configured with Data Integrator

        Yields:
            str     Plugin Name
        """
        for plugin in self._plugin_manager.getPluginsOfCategory('MetaDBPlugins'):
            self.logger.debug('"{}" found under "MetaDBPlugins" category'.format(
                plugin.plugin_object.iplugin_name))
            yield plugin.plugin_object.iplugin_name

    def install_db(self, db_plugin_name):
        """This function should be used to setup the Data Integrator on the current system

        Args:
            db_plugin_name (str):   The plugin name that will be used to install database

        .. warning::
                The current implementation will not check for existing installation and will override the
                existing settings if any exists
        """
        self.logger.info('Initiating the installation process for the Data Integrator')
        self.logger.info('Getting ready to ask setup questions')

        for plugin in self._plugin_manager.getPluginsOfCategory('MetaDBPlugins'):
            if plugin.plugin_object.iplugin_name == db_plugin_name:
                self.logger.debug('"{}" found in the installed plugins and will be configured now'
                                  .format(plugin.plugin_object.iplugin_name))
                metadata_db = plugin.plugin_object
                metadata_db.prompt_details()
                metadata_db.save_details_to_config(self._config)

                answer = confirm('Want to test the saved database settings(y/n): ')
                if answer:
                    self.logger.debug('Testing connectivity of the newly configured database')
                    engine = metadata_db.create_db_engine(self._config)
                    metadata_db.test_db_connection(engine)

    def count_db(self):
        """Provide the number of plugins available for installing database

        Args:
            None
        Returns:
            int
        """
        return len(self._plugin_manager.getPluginsOfCategory('MetaDBPlugins'))

    def test_db(self):
        """Function to test the database connectivity currently configured for Data Integrator
        """
        plugin_found = False
        for plugin in self._plugin_manager.getPluginsOfCategory('MetaDBPlugins'):
            self.logger.debug('"{}" found and will be tested if configured in this system'.format(
                plugin.plugin_object.iplugin_name))
            if plugin.plugin_object.iplugin_name == self._config.get('Database', 'DB_Plugin_Name', 0):
                self.logger.debug('"{}" is configured and will be tested now'.format(
                    plugin.plugin_object.iplugin_name))
                plugin_found = True
                metadata_db = plugin.plugin_object
                engine = metadata_db.create_db_engine(self._config)
                return metadata_db.test_db_connection(engine)

        if not plugin_found:
            self.logger.warning('No meta database is configured. Please configure an db using "install" command')
            print('WARNING: No database is configured. Use "install" command to configure it else DI will not work')
            return False


if __name__ == '__main__':
    pass
