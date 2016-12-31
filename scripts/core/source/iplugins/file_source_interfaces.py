"""
.. module:: scripts.core.source.file_source.py
        :platform: Unix, Windows
        :synopsis: IPlugin interface for file source used in Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from yapsy.IPlugin import IPlugin
from ..file_source import FileSource


class IFileSource(IPlugin, FileSource):
    """Iplugin interface class for File Sources. All plugins related to
        file source should inherit this interface to be recogonized in
        Data Integrator
    """

    iplugin_name = None

    def __init__(self, source_name, file_name, file_path):
        """IFileSource constructor to initialize the file source

        Args:
            source_name (str):  Unique name of the source in the DI project
            file_name (str): The file on the file system that will be used as source
            file_path (str): Path to the file passed as above argument
        """
        super(self.__class__, self).__init__(source_name, file_name, file_path)

