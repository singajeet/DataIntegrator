"""
.. module:: plugins.manage_setup.meta_sqllite_mem.py
        :platform: Unix, Windows
        :synopsis: Plugin to store the metadata in the Sqllite memory database

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
import scripts.core.manage_setup.iplugins as plugintypes


class SqlLiteMetadataDatabase(plugintypes.IMetadataDatabasePlugin):
    """This class will be used to store the metadata information of SqlLite Database
    """
    iplugin_name = 'SqlLiteMetadataDatabasePlugin'

    def __init__(self):
        plugintypes.IMetadataDatabasePlugin.__init__(self)
        self.dbtype = self.DBTYPE_SQLLITE_MEM
