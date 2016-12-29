"""
.. module:: scripts.core.manage_setup.install.py
        :platform: Unix, Windows
        :synopsis: Module to install and configure the Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from __future__ import unicode_literals
import logging
from config.config_manager import ConfigManager
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import confirm
from yapsy.PluginManager import PluginManager
from .iplugins import IMetadataDatabasePlugin


class SetupManager:
    """Setup Manager class is used to create and manage Data Integrator projects

    """

    logger = logging.getLogger('{}.SetupManager'.format(__package__))

    def __init__(self):
        """Initializer of Project Manager

                Project **logging** & **configuration** will be initialized in this class
        """
        # self.logger.setLevel(level=logging.DEBUG)
        self.logger.info('Trying to load the configuration file...')
        self.config = ConfigManager()
        self.logger.info('Config Manager has been initiated using config file: ' + self.config.config_file_name)
        self.plugin_manager = PluginManager(categories_filter={"MetaDBPlugins": IMetadataDatabasePlugin})
        self.plugin_manager.setPluginPlaces([self.config.get('Plugins', 'setup_manager_plugins', 0)])
        self.plugin_manager.locatePlugins()
        self.plugin_manager.loadPlugins()

    def list(self):
        """Provides the list of all installed plugins that can be configured with Data Integrator
        """
        for plugin in self.plugin_manager.getPluginsOfCategory('MetaDBPlugins'):
            self.logger.debug('"{}" found under "MetaDBPlugins" category'.format(
                plugin.plugin_object.iplugin_name))
            yield plugin.plugin_object.iplugin_name

    def install(self, db_plugin_name):
        """This function should be used to setup the Data Integrator on the current system

        .. warning::
                The current implementation will not check for existing installation and will override the
                exisiting settings if any exists
        """
        self.logger.info('Initiating the installation process for the Data Integrator')
        self.logger.info('Getting ready to ask setup questions')

        # self.dbtype = int(prompt('Database type[0=Oracle, 1=Cx_Oracle, 2=Sqllite_Mem, 3=Sqllite_file]: '))

        for plugin in self.plugin_manager.getPluginsOfCategory('MetaDBPlugins'):
            if plugin.plugin_object.iplugin_name == db_plugin_name:
                self.logger.debug('"{}" found in the installed plugins and will be configured now'.format(plugin.plugin_object.iplugin_name))
                self.metadata_db = plugin.plugin_object
                self.metadata_db.prompt_details()
                self.metadata_db.save_details_to_config(self.config)

                answer = confirm('Want to test the saved database settings(y/n): ')
                if answer:
                    self.logger.debug('Testing connectivity of the newly configured database')
                    engine = self.metadata_db.create_db_engine(self.config)
                    self.metadata_db.test_db_connection(engine)

    def test_database(self):
        """Function to test the database connectivity currently configured for Data Integrator
        """
        plugin_found = False
        for plugin in self.plugin_manager.getPluginsOfCategory('MetaDBPlugins'):
            self.logger.debug('"{}" found and will be tested if configured in this system'.format(
                plugin.plugin_object.iplugin_name))
            if plugin.plugin_object.iplugin_name == self.config.get('Database', 'DB_Plugin_Name', 0):
                self.logger.debug('"{}" is configured and will be tested now'.format(
                    plugin.plugin_object.iplugin_name))
                plugin_found = True
                self.metadata_db = plugin.plugin_object
                engine = self.metadata_db.create_db_engine(self.config)
                return self.metadata_db.test_db_connection(engine)

        if not plugin_found:
            self.logger.warning('No meta database is configured. Please configure an db using "install" command')
            print('WARNING: No database is configured. Use "install" command to configure it else DI will not work')
            return False


if __name__ == '__main__':
    pass
