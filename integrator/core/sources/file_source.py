"""
.. module:: scripts.core.source.file_source.py
        :platform: Unix, Windows
        :synopsis: Abstract class for file source used in Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""

from .source_abstract import Source


class FileSource(Source):
    """An abstract class for the File Source type.
        This class accepts an instance of class:
        :class:`scripts.core.data_object.iplugins.file_type_interfaces.IFile`
        All file source should be inherited from this class
    """
    _source_type = None
    _file = None

    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, value):
        self._file = value

    def __init__(self, source_name, pfile):
        """File Source class constructor to create an instance

        Args:
            source_name (str): Name of the file source
            pfile (scripts.core.data_object.iplugins.file_type_interfaces.IFile): An instance of the File class

        :type pfile: scripts.core.data_object.iplugins.files.IFile
        """
        self._source_name = source_name
        self._file = pfile

    def read(self):
        pass

    def write(self):
        pass

    def load_data(self):
        pass

    def dump_data(self):
        pass
