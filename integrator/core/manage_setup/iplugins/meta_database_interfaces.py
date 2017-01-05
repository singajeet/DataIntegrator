"""
.. module:: scripts.core.manage_setup.iplugins.py
        :platform: Unix, Windows
        :synopsis: Define the plugin interface for all supported meta db

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from yapsy.IPlugin import IPlugin


class IMetadataDatabasePlugin(IPlugin):
    """Base class for the Metadata Database details

    """

    def __init__(self):
        super(IMetadataDatabasePlugin, self).__init__()

    _iplugin_name = None
    _dbname = None
    _dbtype = None
    _metadatadbconnection = None

    @property
    def iplugin_name(self):
        return self._iplugin_name

    @iplugin_name.setter
    def iplugin_name(self, value):
        self._iplugin_name = value

    @iplugin_name.deleter
    def iplugin_name(self):
        del self._iplugin_name

    @property
    def dbname(self):
        return self._dbname

    @dbname.setter
    def dbname(self, value):
        self._dbname = value

    @dbname.deleter
    def dbname(self):
        del self._dbname

    @property
    def dbtype(self):
        return self._dbtype

    @dbtype.setter
    def dbtype(self, value):
        self._dbtype = value

    @dbtype.deleter
    def dbtype(self):
        del self._dbtype

    @property
    def metadatadbconnection(self):
        return self._metadatadbconnection

    @metadatadbconnection.setter
    def _metadatadbconnection(self, value):
        self._metadatadbconnection = value

    def prompt_details(self):
        pass

    def get_connection_string(self):
        pass

    def print_details_as_logs(self):
        pass

    def save_details_to_config(self, config):
        pass

    def load_details_from_config(self, config):
        pass

    def create_db_engine(self, config):
        pass

    def test_db_connection(self, engine):
        pass

    def close_db_session(self, engine):
        pass

    """Below are the type supported by DI as of now
    """
    DBTYPE_ORACLE = 'DBTYPE_ORACLE'
    DBTYPE_CX_ORACLE = 'DBTYPE_CX_ORACLE'
    DBTYPE_SQLITE_MEM = 'DBTYPE_SQLITE_MEM'
    DBTYPE_SQLITE_FILE = 'DBTYPE_SQLITE_FILE'
    DBTYPE_MSSQL = 'DBTYPE_MSSQL'
