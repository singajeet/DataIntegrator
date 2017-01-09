"""
.. module:: scripts.core.source.file_source.py
        :platform: Unix, Windows
        :synopsis: IPlugin interface for file source used in Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from yapsy.IPlugin import IPlugin
from integrator.core.interfaces.sources import ISource
from flufl.i18n import initialize

_ = initialize(__file__)


class FileSourceNotImplementedError(Exception):
    """Exception to raise when file source is not implemented
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class IFileSource(ISource, IPlugin):
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
