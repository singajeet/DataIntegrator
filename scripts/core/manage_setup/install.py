"""
.. module:: scripts.core.manage_project.install.py
    :platform: Unix, Windows
    :synopsis: Module to install and configure the Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from ..logger import Logger
from ..config_manager import ConfigManager

class ProjectManager:
  """Project Manager class is used to create and manage Data Integrator projects

  """

  def __init__(self):
    """Initializer of Project Manager

        Project **logging** & **configuration** will be initialized in this class
    """
    self.logger = Logger()
    self.config = ConfigManager()
