"""
.. module:: scripts.core.source.source_abstract.py
        :platform: Unix, Windows
        :synopsis: Abstract definition of source used in Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""


class Source(object):
    """Base class for an source used in Data Integrator
    """
    source_name = None
    source_type = None

    """Source type currently supported in Data Integrator
    """
    FILE_SOURCE_TYPE = 'FILE_SOURCE_TYPE'
    IN_MEMORY_SOURCE_TYPE = 'IN_MEMORY_SOURCE_TYPE'
    DATABASE_SOURCE_TYPE = 'DATABASE_SOURCE_TYPE'
    WEB_SERVICE_SOURCE_TYPE = 'WEB_SERVICE_SOURCE_TYPE'
