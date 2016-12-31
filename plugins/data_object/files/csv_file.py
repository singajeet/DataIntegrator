"""
.. module:: plugins.data_object.files.csv_file.py
        :platform: Unix, Windows
        :synopsis: Plugin implementation for CSV file data object type used in Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
import scripts.core.data_object.iplugins.files as plugintypes
import logging
import csv


class CSVFilePlugin(plugintypes.IFile):
    """File plugin for csv file operations. For more details,
        please refer to the documentation of built-in file functions
    """

    logger = logging.getLogger('{}.CSVFilePlugin'.format(__package__))

    def __init__(self):
        plugintypes.IFile.__init__(self)
        self._iplugin_name = self.CSV_FILE

    def open(self, name, mode='r', buffering=-1, encoding=None, errors=None,
             newline=None, closefd=None, opener=None):
        try:
            self._handle = open(name, mode, buffering, encoding, errors,
                                newline, closefd, opener)
            return self._handle
        except IOError as ex:
            self.logger.error('Can\'t open file in read/write mode: {}'.format(ex.message))
            raise

    def reader(self):
        try:
            csv_reader = csv.reader(self._handle, delimiter=',', quotechar='"')
            return csv_reader
        except Exception as ex:
            self.logger.error('Can\'t open file in read/write mode: {}'.format(ex.message))
            raise