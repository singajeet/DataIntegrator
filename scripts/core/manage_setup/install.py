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


class SetupManager:
    """Setup Manager class is used to create and manage Data Integrator projects

    """

    logger = logging.getLogger(__package__ + '.SetupManager')

    def __init__(self):
        """Initializer of Project Manager

                Project **logging** & **configuration** will be initialized in this class
        """
        # self.logger.setLevel(level=logging.DEBUG)
        self.logger.info('Trying to load the configuration file...')
        self.config = ConfigManager()
        self.logger.info('Config Manager has been initiated using config file: ' + self.config.config_file_name)

    def install(self):
        """This function should be used to setup the Data Integrator on the current system

        .. warning::
                The current implementation will not check for existing installation and will override the
                exisiting settings if any exists
        """
        self.logger.info('Initiating the installation process for the Data Integrator')
        self.logger.info('Getting ready to ask setup questions')

        self.dbtype = int(prompt('Database type[0=Oracle, 1=Cx_Oracle, 2=Sqllite_Mem, 3=Sqllite_file]: '))

        if self.dbtype == MetadataDatabase.DBTYPE_ORACLE:
            self.metadata_db = OracleMetadataDatabase()
            self.metadata_db.prompt_details()
            self.metadata_db.save_details_to_config(self.config)

        answer = confirm('Want to test the saved database settings(y/n): ')
        if answer == 'y':
            self.logger.debug('Want to test db settings: User selection => %s'.format(answer))
            engine = self.metadata_db.create_db_engine(self.config)
            self.metadata_db.test_db_connection(engine)

    def test_database(self):
        self.metadata_db = OracleMetadataDatabase()
        engine = self.metadata_db.create_db_engine(self.config)
        self.metadata_db.test_db_connection(engine)


if __name__ == '__main__':
    pass
