"""
.. module:: scripts.core.interfaces.data_objects
        :platform: Unix, Windows
        :synopsis: Abstract class for file data object type used in Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
import enum


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


class IDataObjectType(enum.Enum):
    """Data object types supported in DI
    """
    FILE = 1
    TABLE = 2
    DB_TABLE = 3
    OTHERS = -1


class IFile:
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
