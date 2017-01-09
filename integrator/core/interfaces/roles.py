"""
.. module:: integrator.core.interfaces.roles
        :platform: Unix, Windows
        :synopsis: Interface to be implemented by servers, groups and users

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
import enum


class IRole:
    """This interface should be implemented by all roles
    """

    _role_name = None
    _role_type = None

    @property
    def role_name(self):
        return self._role_name

    @role_name.setter
    def role_name(self, value):
        self._role_name = value

    @property
    def role_type(self):
        return self._role_type


class IRoleType(enum.Enum):
    """various role types that will be supported in DI
    """
    USER = 1
    GROUP = 2
    SERVER = 3
    OTHERS = -1
