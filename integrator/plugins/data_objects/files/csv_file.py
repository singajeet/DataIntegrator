"""
.. module:: plugins.data_object.files.csv_file.py
        :platform: Unix, Windows
        :synopsis: Plugin implementation for CSV file data object type used in Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
import integrator.core.interfaces.data_objects as interfaces
from flufl.i18n import initialize
import logging
import odo

_ = initialize(__file__)


class CSVFile(interfaces.IFile):
    """File plugin for csv file operations. For more details,
        please refer to the documentation of built-in file functions
    """

    logger = logging.getLogger('{}.CSVFile'.format(__package__))
    _kwds = None
    _encoding = None
    _header = False

    def __init__(self):
        """Constructor to initialize the CSV file load process
            and store data in the internal :mod:`Pandas`.:class:`DataFrame' table
        Args:
            file_name (str): File name with full path to the CSV file
            has_header (bool): Flag whether the CSV includes header or not
        """
        interfaces.IFile.__init__(self)
        self._iplugin_name = 'CSVFilePlugin'
        self._file_type = interfaces.IFileType.CSV

    def setup_csv_file(self, file_name, has_header=None, **kwds):
        self._file_name = file_name
        self._kwds = kwds
        try:
            if has_header is None or has_header is False:
                self._header = False
            else:
                self._header = True
            self._table = odo.odo(file_name, has_header=self._header)
        except Exception as ex:
            self.logger.error(_('Unable to open file due to error: %s') % ex.message)
            raise

    def get_pandas_dataframe(self):
        return self._table

    def _prepare_model(self, model_name):
        """Internal function to prepare data model of the CSV file loaded
        Args:
            model_name (str): The new model of CSV data will
                                have class name mentioned in this parameter
        """
        try:
            if self._table.columns is not None:
                cls_attributes = {}
                for column in self._table.columns:
                    # Prepare column name as class attributes
                    cls_attributes[column] = self._table[column]
            else:
                raise self.CsvModelColumnMissingError(self._table)
        except Exception as ex:
            self.logger.error(_('Unable to prepare data model due to error: %s') % ex.message)
            raise

    """============================================================================
    #
    #   Below section contains classes related to exceptions and other metaclasses
    #
    ============================================================================"""
    class CsvModelColumnMissingError(Exception):
        """Raised when the csv table do not have the columns defined
        """
        logger = logging.getLogger('{}.CSVFile.CsvModelColumnMissingError'.format(__package__))
        expression = _('ColumnMissingError: Unable to find columns in data frame')
        message = _('ColumnMissingError: Atleast one column is required in csv file')

        def __init__(self, object_name):
            self.logger.error(self.expression.format(object_name))
            self.logger.error(self.message)


if __name__ == '__main__':
    pass
