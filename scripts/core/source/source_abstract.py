"""
.. module:: scripts.core.source.source_abstract.py
        :platform: Unix, Windows
        :synopsis: Abstract definition of source used in Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""


class Source(object):
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

    """Source type currently supported in Data Integrator
    """
    FILE_SOURCE_TYPE = 'FILE_SOURCE_TYPE'
    IN_MEMORY_SOURCE_TYPE = 'IN_MEMORY_SOURCE_TYPE'
    DATABASE_SOURCE_TYPE = 'DATABASE_SOURCE_TYPE'
    WEB_SERVICE_SOURCE_TYPE = 'WEB_SERVICE_SOURCE_TYPE'
