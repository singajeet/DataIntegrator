"""
.. module:: integrator.core.interfaces.servers
        :platform: Unix, Windows
        :synopsis: Interface to be implemented by all Threads/Process

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
import enum


class IServer:
    """This interface should be implemeted by all the server classes
    """

    _server_name = None
    _server_type = None

    @property
    def server_name(self):
        return self._server_name

    @server_name.setter
    def server_name(self, value):
        self._server_name = value

    @property
    def server_type(self):
        return self._server_type


class IServerType(enum.Enum):
    """Various server type supported by DI
    """

    LOG = 1
    OTHERS = -1
