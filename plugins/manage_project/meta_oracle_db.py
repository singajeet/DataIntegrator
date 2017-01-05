"""
.. module:: plugins.manage_setup.meta_oracle_db.py
        :platform: Unix, Windows
        :synopsis: Plugin to store the metadata in the Oracle database

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from __future__ import unicode_literals
import logging
from prompt_toolkit import prompt
from sqlalchemy import create_engine
import integrator.core.manage_project.iplugins.meta_database_interfaces as plugintypes
from flufl.i18n import initialize

_ = initialize(__file__)


class OracleMetadataDatabasePlugin(plugintypes.IMetadataDatabasePlugin):
    """This class will be used to store the metadata information of Oracle Database
    """

    _iplugin_name = 'OracleMetadataDatabasePlugin'
    logger = logging.getLogger('{}.OracleMetadataDatabasePlugin'.format(__package__))
    _dbhost = None
    _dbport = None
    _dbservice = None
    _dbuser = None
    _dbpassword = None
    _metadatadbconnection = None
    _dbengine = None

    def __init__(self):
        plugintypes.IMetadataDatabasePlugin.__init__(self)
        self._dbtype = self.DBTYPE_ORACLE

    def prompt_details(self):
        """This function will prompt for database details from user

        Args:
            None.

        Returns:
            None.
        """
        self.logger.debug(_('Prompting user for database details'))

        self._dbname = prompt(_('Database Name to be stored in config: '))
        self._dbhost = prompt(_('Hostname: '))
        self._dbport = prompt(_('Port: '))
        self._dbservice = prompt(_('Service: '))
        self._dbuser = prompt(_('Username: '))
        self._dbpassword = prompt(_('Password: '), is_password=True)
        self.print_details_as_logs()
        self.logger.debug(_('All details collected successfully from user'))

    def get_connection_string(self):
        """This function will return the URI to connect with Oracle database

        Args:
            None.

        Returns:
            str.
        """
        return 'oracle://{}:{}@{}:{}/{}'.format(self._dbuser, self._dbpassword, self._dbhost, self._dbport, self._dbservice)

    def print_details_as_logs(self):
        """This function will just log the details of database

        Returns:
            None
        """
        self.logger.debug(_('Below are the database detalis...'))
        self.logger.debug(_('DB Name: %s | DB Type: %s | DB Host: %s | DB Port: %s') % (
            self._dbname,
            self._dbtype,
            self._dbhost,
            self._dbport))
        self.logger.debug(_('DB Service: %s | DB Username: %s') % (self._dbservice, self._dbuser))

    def save_details_to_config(self, config):
        """This function will save the db details to config object passed as argument

        Args:
            config (fileConfig):    object pointing to the :mod:`ConfigParser` object

        Returns:
            None.
        """
        try:
            self.logger.debug(_('Saving settings to config file'))
            if not config.config.has_section('Database'):
                config.add_section('Database')

            config.set('Database', 'DB_Name', self._dbname)
            config.set('Database', 'DB_Type', self._dbtype)
            config.set('Database', 'DB_Host', self._dbhost)
            config.set('Database', 'DB_Port', self._dbport)
            config.set('Database', 'DB_Service', self._dbservice)
            config.set('Database', 'DB_Username', self._dbuser)
            config.set('Database', 'DB_Password', self._dbpassword)
            config.set('Database', 'DB_Plugin_Name', self._iplugin_name)

            self._metadatadbconnection = self.get_connection_string()
            config.set('Database', 'Metadata_db_connection', self._metadatadbconnection)
            config.save()
            self.print_details_as_logs()
            self.logger.debug(_('Settings saved successfully!'))
        except Exception as ex:
            self.logger.error(_('Unable to save settings due to: %s') % (ex.message))

    def load_details_from_config(self, config):
        """Load details of database from configuration file

        Args:
            config (fileConfig):    object pointing to the :mod:`ConfigParser` object

        Returns:
            None
        """
        try:
            self.logger.debug(_('Loading database settings'))
            self._dbname = config.get('Database', 'DB_Name', 0)
            self._dbtype = config.get('Database', 'DB_Type', 0)
            self._dbhost = config.get('Database', 'DB_Host', 0)
            self._dbport = config.get('Database', 'DB_Port', 0)
            self._dbservice = config.get('Database', 'DB_Service', 0)
            self._dbuser = config.get('Database', 'DB_Username', 0)
            self._dbpassword = config.get('Database', 'DB_Password', 0)
            self._iplugin_name = config.get('Database', 'DB_Plugin_Name', 0)
            self._metadatadbconnection = config.get('Database', 'Metadata_db_connection', 0)
            self.print_details_as_logs()
            self.logger.debug(_('Settings loaded successfully!'))
        except Exception as ex:
            self.logger.error(_('Unable to load database settings due to: %s') % (ex.message))

    def create_db_engine(self, config):
        """Function to create database engine object for Oracle database

        Args:
            config (:mod:`ConfigParser`):  an instance of :mod:`ConfigParser`

        Returns:
            :mod:`SQLAlchemy`.:class:`Engine`
        """
        try:
            self.load_details_from_config(config)
            self.logger.debug(_('Creating db engine: %s') % (self._dbname))
            self.logger.debug(_('Using DB connection uri: %s') % (self._metadatadbconnection))

            self._dbengine = create_engine(self._metadatadbconnection)

            self.logger.debug(_('DB engine created successfully!'))
            return self._dbengine
        except Exception as ex:
            self.logger.error(_('Unable to create db engine due to: %s') % (ex.message))

    def test_db_connection(self, engine):
        """Function to test db connection with Oracle database. Returns `True` is success else `False`

        Args:
            engine (:mod:`SQLAlchemy`.:class:`Connection`)

        Returns:
            bool
        """
        try:
            self.logger.debug(_('Connecting to database using engine: %s') % (engine))
            self.logger.debug(_('Using query: "SELECT 1 FROM DUAL"'))

            connection = engine.connect()
            result = connection.select('select 1 from dual')
            for r in result:
                print(r)
            connection.close()
            self.logger.debug(_('Query executed successfully!'))
            return True
        except Exception as ex:
            self.logger.error(_('Database connection failed') % (ex.message))
            return False

    def close_db_session(self, connection):
        """Function to close the database connection

        Args:
            engine (:mod:`SQLAlchemy`.:class:`Connection`)

        Returns:
            None
        """
        try:
            self.logger.debug(_('Closing database connection'))
            connection.close()
            self.logger.debug(_('Database connection closed successfully!'))
        except Exception as ex:
            self.logger.error(_('Unable to close database connection: {}') % (ex.message))
