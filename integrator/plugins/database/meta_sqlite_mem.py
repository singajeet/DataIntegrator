"""
.. module:: plugins.manage_setup.meta_sqllite_mem.py
        :platform: Unix, Windows
        :synopsis: Plugin to store the metadata in the Sqllite memory database

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
import integrator.core.interfaces.meta_databases as interfaces
import logging
from pony.orm import Database, db_session
from flufl.i18n import initialize

_ = initialize(__file__)


class SqliteMetadataDatabase(interfaces.IMetadataDatabasePlugin):
    """This class will be used to store the metadata information of SqlLite Database
    """
    _iplugin_name = 'SqliteMetadataDatabasePlugin'
    logger = logging.getLogger('{}.SqliteMemMetadataDatabasePlugin'.format(__package__))
    _dbengine = None

    def __init__(self):
        interfaces.IMetadataDatabasePlugin.__init__(self)
        self._dbtype = self.DBTYPE_SQLITE_MEM

    def prompt_details(self):
        """An empty implementation of this function as Sqlite Mem do not require any configuration strings

        Returns:
            None
        """
        self.logger.debug(_('No configuration required for Sqlite'))
        print(_('No configuration to change for Sqlite'))

    def get_connection_string(self):
        """This function will return the URI to connect with Sqlite Memory database

        Returns:
            str
        """
        return ':memory:'

    def print_details_as_logs(self):
        """This function will just log the details of database

        Returns:
            None
        """
        self.logger.debug(_('Below are the database details...'))
        self.logger.debug(_('DB Name: %s | DB Type: %s | DB uri: %s') % (
            self._dbname, self._dbtype, self._metadatadbconnection))

    def save_details_to_config(self, config):
        """This function will populate default db details for Sqlite in-memory db
        """
        self.logger.debug(_('No configuration to save for Sqlite'))
        self._dbname = 'Sqlite In-Memory'
        self._dbtype = self.DBTYPE_SQLITE_MEM
        self._metadatadbconnection = ':memory:'
        self.print_details_as_logs()

    def load_details_from_config(self, config):
        """Load details of database. Since this is an in-memory database so nothing will be loaded from config file

        Args:
            config (fileConfig): could be left as None as it will not be used to load configuration

        Returns:
            None
        """
        self.logger.debug(_('No configuration to load for Sqlite'))
        self._dbname = 'Sqlite In-Memory'
        self._dbtype = self.DBTYPE_SQLITE_MEM
        self._metadatadbconnection = self.get_connection_string()
        self.print_details_as_logs()

    def create_db_engine(self, config):
        """Function to create database engine object for Sqlite database

        Args:
            config (:mod:`ConfigParser`):  an instance of :mod:`ConfigParser`

        Returns:
            :mod:`PonyOrm`.:class:`Database`
        """
        try:
            self.logger.debug(_('Creating db engine: %s') % (self._dbname))
            self.logger.debug(_('Using DB connection uri: %s') % (self._metadatadbconnection))

            self._dbengine = Database()
            self._dbengine.bind('sqlite', self.metadatadbconnection)

            self.logger.debug(_('DB engine created successfully!'))
            return self._dbengine
        except Exception as ex:
            self.logger.error(_('Unable to create db engine due to: %s') % (ex.message))

    def test_db_connection(self, engine):
        """Function to test db connection with Sqlite database. Returns `True` is success else `False`

        Args:
            engine (:mod:`PonyOrm`.:class:`Database`)

        Returns:
            bool
        """
        try:
            self.logger.debug(_('Connecting to database using engine: %s') % (engine))
            self.logger.debug(_('Using query: "SELECT 1"'))
            with db_session:
                result = engine.select('select 1')
                for r in result:
                    print(r)
            engine.disconnect()
            self.logger.debug(_('Query executed successfully!'))
            return True
        except Exception as ex:
            self.logger.error(_('Database connection failed: %s') % (ex.message))
            return False

    def close_db_session(self, engine):
        """Function to close the database connection

        Args:
            engine (:mod:`PonyOrm`.:class:`session`)

        Returns:
            None
        """
        try:
            self.logger.debug(_('Closing database connection'))
            engine.disconnect()
            self.logger.debug(_('Database connection closed successfully!'))
        except Exception as ex:
            self.logger.error(_('Unable to close database connection: %s') % (ex.message))
