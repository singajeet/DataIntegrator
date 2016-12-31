"""
.. module:: scripts.core.source.file_source.py
        :platform: Unix, Windows
        :synopsis: Abstract class for file source used in Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""

from .source_abstract import Source


class FileSource(Source):
    """An abstract class for the File Source type.
        All file source should be inherited from this class
    """
    file_source_type = None
    file_name = None
    file_ext = None
    file_path = None



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

    def __init__(self, source_name, file_name, file_path):
        self.source_name = source_name
        self.file_path = file_path
        self.file_name = file_name
        self.file_ext = (file_name.split('.')).pop()  # Get the file extension from the filename
        self.source_type = self.FILE_SOURCE_TYPE

    def read(self):
        pass

    def write(self):
        pass

    def load_data(self):
        pass

    def dump_data(self):
        pass


