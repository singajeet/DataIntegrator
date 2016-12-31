"""
.. module:: plugins.manage_setup.meta_oracle_db.py
        :platform: Unix, Windows
        :synopsis: Plugin to store the metadata in the Oracle database

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from __future__ import unicode_literals
import logging
from prompt_toolkit import prompt
from pony.orm import Database, db_session
import scripts.core.manage_setup.iplugins.meta_database_interfaces as plugintypes


class OracleMetadataDatabasePlugin(plugintypes.IMetadataDatabasePlugin):
    """This class will be used to store the metadata information of Oracle Database
    """

    iplugin_name = 'OracleMetadataDatabasePlugin'
    logger = logging.getLogger('{}.OracleMetadataDatabasePlugin'.format(__package__))
    dbhost = None
    dbport = None
    dbservice = None
    dbuser = None
    dbpassword = None

    def __init__(self):
        plugintypes.IMetadataDatabasePlugin.__init__(self)
        self.dbtype = self.DBTYPE_ORACLE

    def prompt_details(self):
        """This function will prompt for database details from user

        Args:
            None.

        Returns:
            None.
        """
        self.logger.debug('Prompting user for database details')

        self.dbname = prompt('Database Name to be stored in config: ')
        self.dbhost = prompt('Hostname: ')
        self.dbport = prompt('Port: ')
        self.dbservice = prompt('Service: ')
        self.dbuser = prompt('Username: ')
        self.dbpassword = prompt('Password: ', is_password=True)
        self.print_details_as_logs()
        self.logger.debug('All details collected successfully from user')

    def get_connection_string(self):
        """This function will return the URI to connect with Oracle database

        Args:
            None.

        Returns:
            str.
        """
        return '{}/{}@{}:{}/{}'.format(self.dbuser, self.dbpassword, self.dbhost, self.dbport, self.dbservice)

    def print_details_as_logs(self):
        """This function will just log the details of database

        Args:
            None

        Returns:
            None
        """
        self.logger.debug('Below are the database detalis...')
        self.logger.debug('DB Name: {} | DB Type: {} | DB Host: {} | DB Port: {}'.format(
            self.dbname,
            self.dbtype,
            self.dbhost,
            self.dbport))
        self.logger.debug('DB Service: {} | DB Username: {}'.format(self.dbservice, self.dbuser))

    def save_details_to_config(self, config):
        """This function will save the db details to config object passed as argument

        Args:
            config (fileConfig):    object pointing to the :mod:`ConfigParser` object

        Returns:
            None.
        """
        try:
            self.logger.debug('Trying to save the database details to config file')
            if not config.config.has_section('Database'):
                config.add_section('Database')

            config.set('Database', 'DB_Name', self.dbname)
            config.set('Database', 'DB_Type', self.dbtype)
            config.set('Database', 'DB_Host', self.dbhost)
            config.set('Database', 'DB_Port', self.dbport)
            config.set('Database', 'DB_Service', self.dbservice)
            config.set('Database', 'DB_Username', self.dbuser)
            config.set('Database', 'DB_Password', self.dbpassword)
            config.set('Database', 'DB_Plugin_Name', self.iplugin_name)

            self.metadatadbconnection = self.get_connection_string()
            config.set('Database', 'Metadata_db_connection', self.metadatadbconnection)
            config.save()
            self.print_details_as_logs()
            self.logger.debug('Database details stored to config file successfully!')
        except Exception as ex:
            self.logger.error('Error while saving db configuration: {}'.format(ex.message))

    def load_details_from_config(self, config):
        """Load details of database from configuration file

        Args:
            config (fileConfig):    object pointing to the :mod:`ConfigParser` object

        Returns:
            None
        """
        try:
            self.logger.debug('Trying to load database details from config file')
            self.dbname = config.get('Database', 'DB_Name', 0)
            self.dbtype = config.get('Database', 'DB_Type', 0)
            self.dbhost = config.get('Database', 'DB_Host', 0)
            self.dbport = config.get('Database', 'DB_Port', 0)
            self.dbservice = config.get('Database', 'DB_Service', 0)
            self.dbuser = config.get('Database', 'DB_Username', 0)
            self.dbpassword = config.get('Database', 'DB_Password', 0)
            self.iplugin_name = config.get('Database', 'DB_Plugin_Name', 0)
            self.metadatadbconnection = config.get('Database', 'Metadata_db_connection', 0)
            self.print_details_as_logs()
            self.logger.debug('Database details loaded successfully from config file!')
        except Exception as ex:
            self.logger.error('Error while loading db details from config: {}'.format(ex.message))

    def create_db_engine(self, config):
        """Function to create database engine object for Oracle database

        Args:
            config (:mod:`ConfigParser`):  an instance of :mod:`ConfigParser`

        Returns:
            :mod:`PonyOrm`.:class:`Database`
        """
        try:
            self.load_details_from_config(config)
            self.logger.debug('Creating db engine for database: "{}"'.format(self.dbname))
            self.logger.debug('Using DB connection uri: {}'.format(self.metadatadbconnection))

            self.dbengine = Database()
            self.dbengine.bind('oracle', self.metadatadbconnection)

            self.logger.debug('DB engine created successfully!')
            return self.dbengine
        except Exception as ex:
            self.logger.error('Error while creating db engine: {}'.format(ex.message))

    def test_db_connection(self, engine):
        """Function to test db connection with Oracle database. Returns `True` is success else `False`

        Args:
            session (:mod:`PonyOrm`.:class:`Database`)

        Returns:
            bool
        """
        try:
            self.logger.debug('Connecting to database using engine: {}'.format(engine))
            self.logger.debug('Executing SQL using database: "SELECT 1 FROM DUAL"')
            with db_session:
                result = engine.select('select 1 from dual')
                for r in result:
                    print(r)
            engine.disconnect()
            self.logger.debug('Query executed successfully!')
            return True
        except Exception as ex:
            self.logger.error('Error while testing db connection: {}'.format(ex.message))
            return False

    def close_db_session(self, engine):
        """Function to close the database connection

        Args:
            session (:mod:`Sqlalchemy`.:class:`session`)

        Returns:
            None
        """
        try:
            self.logger.debug('Trying to close db connection/session')
            engine.disconnect()
            self.logger.debug('DB connection/session closed successfully!')
        except Exception as ex:
            self.logger.error('Error while closing db connection/session: {}'.format(ex.message))
