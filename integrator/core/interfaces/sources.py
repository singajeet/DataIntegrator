"""
.. module:: scripts.core.source.file_source.py
        :platform: Unix, Windows
        :synopsis: IPlugin interface for file source used in Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
import enum


class ISource:
    """Base class for an source used in Data Integrator
    """
    _source_name = None
    _source_type = None

    @property
    def source_name(self):
        return self._source_name

    @source_name.setter
    def source_name(self, value):
        self._source_name = value

    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value


class ISourceType(enum.Enum):
    """Source type currently supported in Data Integrator
    """
    FILE = 1
    IN_MEMORY = 2
    DATABASE = 3
    WEB_SERVICE = 4
    OTHERS = -1
