"""
.. module:: integrator.core.interfaces.logs
        :platform: Unix, Windows
        :synopsis: Interface to be implemented by logging module

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from integrator.core.interfaces.servers import IServer
from yapsy.IPlugin import IPlugin
from flufl.i18n import initialize
import enum

_ = initialize(__file__)


class LoggerNotImplementedError(Exception):
    """Error to raise if logger is not implemented by any subclass
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class ILog(IPlugin):
    """Interface to be implemented by logger used in Data Integrator
    """

    _iplugin_name = None
    _logger_type = None

    @property
    def iplugin_name(self):
        return self._iplugin_name

    @iplugin_name.setter
    def iplugin_name(self, value):
        self._iplugin_name = value

    @property
    def logger_type(self):
        return self._logger_type

    @logger_type.setter
    def logger_type(self, value):
        self._logger_type = value

    def debug(self, message):
        raise LoggerNotImplementedError(_('No logger implemented'), _('This method needs to be implemented by an subclass'))

    def info(self, message):
        raise LoggerNotImplementedError(_('No logger implemented'), _('This method needs to be implemented by an subclass'))

    def warning(self, message):
        raise LoggerNotImplementedError(_('No logger implemented'), _('This method needs to be implemented by an subclass'))

    def error(self, message):
        raise LoggerNotImplementedError(_('No logger implemented'), _('This method needs to be implemented by an subclass'))


class ILoggerType(enum.Enum):
    """Type of logger supported by Data Integrator
    """

    NETWORK_SERVER = 1
    FILE = 2
    CONSOLE = 3
    DATABASE = 4
    NOSQL = 5


class ILogServer(ILog, IServer):
    """Interface to be implemented by the log servers
    """

    def start_server(self):
        raise LoggerNotImplementedError(_('No log server implemented'), _('This method needs to be implemented by an subclass'))

    def stop_server(self):
        raise LoggerNotImplementedError(_('No log server implemented'), _('This method needs to be implemented by an subclass'))

    def serve_until_stopped(self):
        raise LoggerNotImplementedError(_('No log server implemented'), _('This method needs to be implemented by an subclass'))
