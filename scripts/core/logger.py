"""
.. module:: scripts.core.logger.py
    :platform: Unix, Windows
    :synopsis: Module will be used to log information in this project

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""

import logging
from logging.config import fileConfig


class Logger:
  """Logger class will be used system wide to log information at common place

  .. note::
          Internally this class uses :mod:`logging` module and the :class:`logging.fileConfig` class,
          so any attribute of the logger package can be accessed using
          **(Logger class object).logger.<logging package attribute name>**
  """

  def __init__(self):
    """Logger class initializer
    """
    fileConfig('logging_config.ini')
    self.logger = logging.getLogger()
    self.logger.debug('Logging service initiated')


  def debug(self, message):
    self.logger.debug(message)


  def error(self, message):
    self.logger.error(message)


  def warning(self, message):
    self.logger.warning(message)


  def info(self, message):
    self.logger.info(message)
