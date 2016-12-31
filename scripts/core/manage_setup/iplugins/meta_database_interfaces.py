"""
.. module:: scripts.core.manage_setup.iplugins.py
        :platform: Unix, Windows
        :synopsis: Define the plugin interface for all supported meta db

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from yapsy.IPlugin import IPlugin
import logging


class IMetadataDatabasePlugin(IPlugin):
    """Base class for the Metadata Database details

    """

    def __init__(self):
        pass

    iplugin_name = None
    logger = logging.getLogger('{}.IMetadataDatabasePlugin'.format(__package__))
    dbname = None
    dbtype = None

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
