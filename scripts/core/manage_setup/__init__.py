"""Manage Project documentation guide

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>

"""

from logging.config import fileConfig
from os import getcwd

fileConfig(''.join([getcwd(), '/scripts/core/log/logging_config.ini']))
