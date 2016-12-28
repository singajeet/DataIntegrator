"""
.. module:: plugins.manage_setup.meta_sqllite_mem.py
        :platform: Unix, Windows
        :synopsis: Plugin to store the metadata in the Sqllite memory database

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from scripts.core.manage_setup.iplugins import IMetadataDatabasePlugin


class SqlLiteMetadataDatabase(IMetadataDatabasePlugin):
    """This class will be used to store the metadata information of SqlLite Database
    """
