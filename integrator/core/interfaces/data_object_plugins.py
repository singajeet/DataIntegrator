"""
.. module:: scripts.core.interfaces.data_object_plugins
        :platform: Unix, Windows
        :synopsis: Abstract class for file data object type used in Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from integrator.core.interfaces.data_objects import IDataObject, IFile
from yapsy.IPlugin import IPlugin
from flufl.i18n import initialize

_ = initialize(__file__)


class FileDataObjectNotImplementedError(Exception):
    """Exception to raise when not implemented in sub classes
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class IFileDataObject(IDataObject, IFile, IPlugin):
    """IFile interface to be used for writing plugins
    """
    _iplugin_name = None

    @property
    def iplugin_name(self):
        return self._iplugin_name

    @iplugin_name.setter
    def iplugin_name(self, value):
        self._iplugin_name = value

    def open(self, filepath):
        raise FileDataObjectNotImplementedError(_('No file data object implemented'), _('This method needs to be implmented by an subclass'))

    def close(self):
        raise FileDataObjectNotImplementedError(_('No file data object implemented'), _('This method needs to be implmented by an subclass'))

    def read(self):
        raise FileDataObjectNotImplementedError(_('No file data object implemented'), _('This method needs to be implmented by an subclass'))

    def write(self, buffer):
        raise FileDataObjectNotImplementedError(_('No file data object implemented'), _('This method needs to be implmented by an subclass'))
