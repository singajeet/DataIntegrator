"""
.. module:: scripts.core.source.file_source.py
        :platform: Unix, Windows
        :synopsis: Definition and declaration of file source used in Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""

from .source_abstract import Source


class FlatFileSource(Source):
    file_type = None
    file_name = None
    file_path = None

    def __init__(self, source_name, file_path, file_name):
        self.source_name = source_name
        self.file_path = file_path
        self.file_name = file_name
        self.source_type = 'FLAT_FILE_TYPE_SOURCE'

    def read(self):
        pass

    def write(self):
        pass

    def load_data(self):
        pass

    def dump_data(self):
        pass
