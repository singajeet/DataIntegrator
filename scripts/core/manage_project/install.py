"""
.. module:: Install.py
    :platform: Unix, Windows
    :synopsis: Module to install and configure the Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""

import ConfigParser
import logging
from logging.config import fileConfig

class ProjectManager:
  """Project Manager class is used to create and manage Data Integrator projects

  """

  def __init__(self):
    """Initializer of Project Manager

        Project **logging** & **configuration** will be initialized in this class
    """
    fileConfig('logging_config.ini')
    self.logger = logging.getLogger()
    self.logger.debug('Logging service initiated')

    self.config = ConfigParser.ConfigParser()
    self.logger.debug('Config Parser initiated')
    self.config.read('Configuration.cfg')
    self.logger.debug('Configuration file Configuration.cfg has been loaded')
