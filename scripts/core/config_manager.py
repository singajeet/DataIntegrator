"""
.. module:: scripts.core.config_manager.py
    :platform: Unix, Windows
    :synopsis: Module to load and use configuration system wide

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""

import ConfigParser

class ConfigManager:
  """Config Manager class will be used to load and store configuration system wide

  """
  def __init__(self):
    """Config Manager will be initialized here
    """
    self.config = ConfigParser.ConfigParser()
    self.config.read('Configuration.cfg')


  def get(self, section, key, is_raw):
    """Get function will read & return the value of key provided as args

    Args:
      section (str):  Name of the section defined in config file
      key (str):  Name of the key defined under the section
      is_raw (number):  Pass value 1 if the value for key needs to be read as raw from config file

    Returns:
      str.  The value for the key provided in the arguments
    """
    return self.config.get(section, key, is_raw)


  def set(self, section, key, value):
    """Set the key-value pair in the config file under the section provided as args

    Args:
      section (str):  Name of the section under which key-value pair needs to be stored
      key (str):  The unique identifier to store the value under an section
      value (str):  The value that needs to be stored for an unique combination of section & key

    Returns:
      None.
    """
    self.config.set(section, key, value)


  def add_section(self, section):
    """Add a new section provided as argument in the config file

    Args:
      section (str):  Name of the new section that needs to be added

    Returns:
      None.
    """
    self.config.add_section(section)


  def remove_section(self, section):
    """Remove a section from the config file.

    Args:
      section(str): Name of the section that needs to be removed from config file

    Returns:
      bool. Returns `True` if section is removed else returns `False`
    """
    self.config.remove_section(section)
