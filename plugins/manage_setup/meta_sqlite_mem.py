"""
.. module:: plugins.manage_setup.meta_sqllite_mem.py
        :platform: Unix, Windows
        :synopsis: Plugin to store the metadata in the Sqllite memory database

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
import scripts.core.manage_setup.iplugins.meta_database_interfaces as plugintypes
import logging
from prompt_toolkit import prompt
from pony.orm import Database, db_session


class SqliteMetadataDatabase(plugintypes.IMetadataDatabasePlugin):
    """This class will be used to store the metadata information of SqlLite Database
    """
    iplugin_name = 'SqliteMetadataDatabasePlugin'
    logger = logging.getLogger('{}.SqliteMemMetadataDatabasePlugin'.format(__package__))

    def __init__(self):
        plugintypes.IMetadataDatabasePlugin.__init__(self)
        self.dbtype = self.DBTYPE_SQLITE_MEM

    def prompt_details(self):
        """An empty implementation of this function as Sqlite Mem do not require any configuration strings

        Args:
            None

        Returns:
            None
        """
        self.logger.debug('Current Sqlite Memory db requires no settings to be stored')
        print('There are no details to configure for this database')
        prompt('Press "Enter" to continue...')

    def get_connection_string(self):
        """This function will return the URI to connect with Sqlite Memory database

        Args:
            None

        Returns:
            str
        """
        return ':memory:'

    def print_details_as_logs(self):
        """This function will just log the details of database

        Args:
            None

        Returns:
            None
        """
        self.logger.debug('Below are the database details...')
        self.logger.debug('DB Name: {} | DB Type: {} | DB uri: {}'.format(self.dbname, self.dbtype, self.metadatadbconnection))

    def save_details_to_config(self, config):
        """This function will populate default db details for Sqlite in-memory db
        """
        self.logger.debug('No configuration details will be saved for Sqlite Memory Database in config file')
        self.dbname = 'Sqlite In-Memory'
        self.dbtype = self.DBTYPE_SQLITE_MEM
        self.metadatadbconnection = ':memory:'
        self.print_details_as_logs()

    def load_details_from_config(self, config):
        """Load details of database. Since this is an in-memory database so nothing will be loaded from config file

        Args:
            config (fileConfig): could be left as None as it will not be used to load configuration

        Returns:
            None
        """
        self.logger.debug('Loading database details for Sqlite in-memory db')
        self.dbname = 'Sqlite In-Memory'
        self.dbtype = self.DBTYPE_SQLITE_MEM
        self.metadatadbconnection = self.get_connection_string()
        self.print_details_as_logs()

    def create_db_engine(self, config):
        """Function to create database engine object for Sqlite database

        Args:
            config (:mod:`ConfigParser`):  an instance of :mod:`ConfigParser`

        Returns:
            :mod:`PonyOrm`.:class:`Database`
        """
        try:
            self.logger.debug('Creating db engine for database: "{}"'.format(self.dbname))
            self.logger.debug('Using DB connection uri: {}'.format(self.metadatadbconnection))

            self.dbengine = Database()
            self.dbengine.bind('sqlite', self.metadatadbconnection)

            self.logger.debug('DB engine created successfully!')
            return self.dbengine
        except Exception as ex:
            self.logger.error('Error while creating db engine: {}'.format(ex.message))

    def test_db_connection(self, engine):
        """Function to test db connection with Sqlite database. Returns `True` is success else `False`

        Args:
            session (:mod:`PonyOrm`.:class:`Database`)

        Returns:
            bool
        """
        try:
            self.logger.debug('Connecting to database using engine: {}'.format(engine))
            self.logger.debug('Executing SQL using database: "SELECT 1"')
            with db_session:
                result = engine.select('select 1')
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



