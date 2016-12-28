"""
.. module:: scripts.core.source.source_abstract.py
        :platform: Unix, Windows
        :synopsis: Abstract definition of source used in Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""


class Source(object):
    source_name = None
    source_type = None
