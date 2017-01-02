"""
.. module:: plugins.data_object.files.csv_file.py
        :platform: Unix, Windows
        :synopsis: Plugin implementation for CSV file data object type used in Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
import scripts.core.data_object.iplugins.files as plugintypes
import logging
import agate


class CSVFilePlugin(plugintypes.IFile):
    """File plugin for csv file operations. For more details,
        please refer to the documentation of built-in file functions
    """

    logger = logging.getLogger('{}.CSVFilePlugin'.format(__package__))
    _kwds = None
    _encoding = None
    _header = False
    columns = None

    def __init__(self, file_name, **kwds):
        plugintypes.IFile.__init__(self)
        self._iplugin_name = 'CSVFilePlugin'
        self._file_type = self.CSV_FILE
        self._file_name = file_name
        self._kwds = kwds
        try:
            self._table = agate.Table.from_csv(self._file_name, delimiter=',', **kwds)
            for column in self._table.column_names:
                setattr(self.columns, column, self._table.columns[column])
        except Exception as ex:
            self.logger.error('Can\'t open csv file due to below error: {}'.format(ex.message))
            raise

    def read_sample(self):
        return self._table.limit(100)

    def get_column_distinct_values(self, column_name):
        self._table.columns[column_name].values_distinct()


if __name__ == '__main__':
    pass
