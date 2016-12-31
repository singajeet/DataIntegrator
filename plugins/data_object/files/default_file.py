"""
.. module:: plugins.data_object.files.default_file.py
        :platform: Unix, Windows
        :synopsis: Plugin implementation for file data object type used in Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
import scripts.core.data_object.iplugins.files as plugintypes
import logging


class DefaultFilePlugin(plugintypes.IFile):
    """File plugin for simple file operations. For more details,
        please refer to the documentation of built-in file functions
    """

    logger = logging.getLogger('{}.DefaultFilePlugin'.format(__package__))

    def __init__(self):
        plugintypes.IFile.__init__(self)
        self._iplugin_name = self.DEFAULT_FILE

    def open(self, name, mode='r', buffering=-1, encoding=None, errors=None,
             newline=None, closefd=None, opener=None):
        try:
            self._handle = open(name, mode, buffering, encoding, errors,
                                newline, closefd, opener)
            return self._handle
        except IOError as ex:
            self.logger.error('Can\'t open file in read/write mode: {}'.format(ex.message))
            raise
