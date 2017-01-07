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
from flufl.i18n import initialize

_ = initialize(__file__)


class ProjectManager:
    """Setup Manager class is used to create and manage Data Integrator projects

    """

    logger = logging.getLogger('{}.ProjectManager'.format(__package__))
    _config = None
    _plugin_manager = None
    _project_name = None

    def __init__(self, project_name):
        """Initializer of Project Manager

                Project **logging** & **configuration** will be initialized in this class
        """
        # self.logging.setLevel(level=logging.DEBUG)
        self.logger.info(_('Loading config file...'))
        self._config = ConfigManager()
        self.logger.info(_('Done! Config file: %s') % self._config.config_file_name)
        self._plugin_manager = PluginManager(categories_filter={"MetaDBPlugins": IMetadataDatabasePlugin})
        self._plugin_manager.setPluginPlaces([self._config.get('Plugins', 'setup_manager_plugins', 0)])
        self._plugin_manager.locatePlugins()
        self._plugin_manager.loadPlugins()
        """Assign the project name to class variable which will be used further in context
        """
        self._project_name = project_name

    def __enter__(self):
        """Context manager will try to open the project provide as arg if found
            else it will create a new project with the name provided in argument
        """
        #   logic to open or create new project
        #
        return self

    def __exit__(self):
        """Context manager will release the resources used and will save the project
        """
        #   release resource and save project
        #

    def list_db(self):
        """Provides the list of all installed plugins that can be configured with Data Integrator

        Yields:
            str     Plugin Name
        """
        for plugin in self._plugin_manager.getPluginsOfCategory('MetaDBPlugins'):
            self.logger.debug(_('Name: %s | Category Type: MetaDBPlugins') % plugin.plugin_object.iplugin_name)
            yield plugin.plugin_object.iplugin_name

    def config_db(self, db_plugin_name):
        """This function should be used to setup the Data Integrator on the current system

        Args:
            db_plugin_name (str):   The plugin name that will be used to install database

        .. warning::
                The current implementation will not check for existing installation and will override the
                existing settings if any exists
        """
        self.logger.info(_('Installing Data Integrator'))
        self.logger.info(_('Preparing info prompts'))

        for plugin in self._plugin_manager.getPluginsOfCategory('MetaDBPlugins'):
            if plugin.plugin_object.iplugin_name == db_plugin_name:
                self.logger.debug(_('%s plugin found. Configuration initiated...') % plugin.plugin_object.iplugin_name)
                metadata_db = plugin.plugin_object
                metadata_db.prompt_details()
                metadata_db.save_details_to_config(self._config)
                self.logger.info(_('Database configured successfully!'))
                answer = confirm(_('Proceed with database settings(y/n): '))
                if answer:
                    self.logger.info(_('Testing database connectivity...'))
                    engine = metadata_db.create_db_engine(self._config)
                    metadata_db.test_db_connection(engine)
                    self.logger.info(_('Connection successfull!'))
        else:
            self.logger.info(_('No database plugin found. Installation aborted!'))

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
        for plugin in self._plugin_manager.getPluginsOfCategory('MetaDBPlugins'):
            self.logger.debug(_('%s plugin found') % plugin.plugin_object.iplugin_name)
            if plugin.plugin_object.iplugin_name == self._config.get('Database', 'DB_Plugin_Name', 0):
                self.logger.info(_('%s plugin is configured. Testing database connectivity...') % plugin.plugin_object.iplugin_name)
                metadata_db = plugin.plugin_object
                engine = metadata_db.create_db_engine(self._config)
                metadata_db.test_db_connection(engine)
                self.logger.info(_('Connection successfull!'))
                return True
        else:
            self.logger.warning(_('No database plugin found. Testing aborted!'))
            self.logger.warning(_('WARNING: No database is configured. Please check documentation for more details'))
            return False

    def config_core(self):
        pass

    def config_cli(self):
        pass

    def config_plugin(self):
        pass

    def config_template(self):
        pass

    def config_security(self):
        pass


if __name__ == '__main__':
    pass
