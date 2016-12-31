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
    _handle = None

    def __init__(self):
        IPlugin.__init__(self)

    @property
    def iplugin_name(self):
        return self._iplugin_name

    @iplugin_name.setter
    def iplugin_name(self, value):
        self._iplugin_name = value

    @property
    def handle(self):
        return self._handle

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
