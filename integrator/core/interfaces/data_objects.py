"""
.. module:: scripts.core.interfaces.data_objects
        :platform: Unix, Windows
        :synopsis: Abstract class for file data object type used in Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from constantly import NamedConstant, Names
from yapsy.IPlugin import IPlugin


class IDataObject:
    """Interface to be implemented by all data objects
    """
    _data_object_name = None
    _data_object_type = None

    @property
    def data_object_name(self):
        return self._data_object_name

    @data_object_name.setter
    def data_object_name(self, value):
        self._data_object_name = value

    @property
    def data_object_type(self):
        return self._data_object_type


class IDataObjectType(Names):
    """Data object types supported in DI
    """
    FILE = NamedConstant()
    TABLE = NamedConstant()
    DB_TABLE = NamedConstant()
    OTHERS = NamedConstant()


class IFile(IPlugin):
    """Interface for file entities in DI
    """
    _file_type = None
    _file_name = None

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value

    @property
    def file_type(self):
        return self._file_type


class IFileType(Names):
    """File source types supported by current implementation of Data Integrator
        """
    DEFAULT = NamedConstant()
    CSV = NamedConstant()
    DELIMITED = NamedConstant()
    ZIP = NamedConstant()
    XLS = NamedConstant()
    XLSX = NamedConstant()
    JSON = NamedConstant()
    XML = NamedConstant()
    HTML = NamedConstant()
    OTHERS = NamedConstant()
