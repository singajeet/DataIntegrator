"""
.. module:: scripts.core.source.file_source.py
        :platform: Unix, Windows
        :synopsis: IPlugin interface for file source used in Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from yapsy.IPlugin import IPlugin
from ..file_source import FileSource


class IFileSource(FileSource, IPlugin):
    """Iplugin interface class for File Sources. All plugins related to
        file source should inherit this interface to be recognized in
        Data Integrator
    """

    _iplugin_name = None

    @property
    def iplugin_name(self):
        return self._iplugin_name

    @iplugin_name.setter
    def iplugin_name(self, value):
        self._iplugin_name = value

    """File source types supported by current implementation of Data Integrator
        """
    CSV_FILE_SOURCE_TYPE = 'CSV_FILE_SOURCE_TYPE'
    DELIMITED_FILE_SOURCE_TYPE = 'DELIMITED_FILE_SOURCE_TYPE'
    ZIP_FILE_SOURCE_TYPE = 'ZIP_FILE_SOURCE_TYPE'
    XLS_FILE_SOURCE_TYPE = 'XLS_FILE_SOURCE_TYPE'
    XLSX_FILE_SOURCE_TYPE = 'XLSX_FILE_SOURCE_TYPE'
    JSON_FILE_SOURCE_TYPE = 'JSON_FILE_SOURCE_TYPE'
    XML_FILE_SOURCE_TYPE = 'XML_FILE_SOURCE_TYPE'
    HTML_FILE_SOURCE_TYPE = 'HTML_FILE_SOURCE_TYPE'

    def __init__(self, source_name, pfile):
        """IFileSource constructor to initialize the file source

        Args:
            source_name (str):  Unique name of the source in the DI project
            pfile (:class:`scripts.core.data_object.iplugins.files.IFile`):
            The file on the file system that will be used as source
        """
        FileSource.__init__(self, source_name, pfile)
