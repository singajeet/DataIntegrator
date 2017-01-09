"""
.. module:: scripts.core.data_object.iplugins.file_type_interfaces.py
        :platform: Unix, Windows
        :synopsis: Abstract class for file data object type used in Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from yapsy.IPlugin import IPlugin
import enum
from flufl.i18n import initialize

_ = initialize(__file__)


class DataObjectNotImplementedError(Exception):
    """
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class IFile(IPlugin):
    """IFile interface to be used for writing plugins
    """
    _iplugin_name = None
    _table = None
    _file_type = None
    _file_name = None

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


class IFileType(enum.Enum):
    """File source types supported by current implementation of Data Integrator
        """
    DEFAULT = 1
    CSV = 2
    DELIMITED = 3
    ZIP = 4
    XLS = 5
    XLSX = 6
    JSON = 7
    XML = 8
    HTML = 9
    OTHERS = -1
