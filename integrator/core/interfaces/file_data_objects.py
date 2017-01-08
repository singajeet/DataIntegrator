"""
.. module:: scripts.core.data_object.iplugins.file_type_interfaces.py
        :platform: Unix, Windows
        :synopsis: Abstract class for file data object type used in Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from yapsy.IPlugin import IPlugin


class IFile(IPlugin):
    """IFile interface to be used for writing plugins
    """
    _iplugin_name = None
    _table = None
    _file_type = None
    _file_name = None

    def __init__(self):
        IPlugin.__init__(self)

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value

    @property
    def iplugin_name(self):
        return self._iplugin_name

    @iplugin_name.setter
    def iplugin_name(self, value):
        self._iplugin_name = value

    @property
    def table(self):
        return self._table

    """File source types supported by current implementation of Data Integrator
        """
    DEFAULT_FILE = 'DEFAULT_FILE'
    CSV_FILE = 'CSV_FILE'
    DELIMITED_FILE = 'DELIMITED_FILE'
    ZIP_FILE = 'ZIP_FILE'
    XLS_FILE = 'XLS_FILE'
    XLSX_FILE = 'XLSX_FILE'
    JSON_FILE = 'JSON_FILE'
    XML_FILE = 'XML_FILE'
    HTML_FILE = 'HTML_FILE'
