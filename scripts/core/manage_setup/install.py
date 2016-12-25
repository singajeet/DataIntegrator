"""
.. module:: scripts.core.manage_project.install.py
    :platform: Unix, Windows
    :synopsis: Module to install and configure the Data Integrator

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from __future__ import unicode_literals
import logging
from ..config.config_manager import ConfigManager
from prompt_toolkit import prompt
from sqlalchemy import create_engine
from sqlalchemy import


class SetupManager:
  """Project Manager class is used to create and manage Data Integrator projects

  """

  logger = logging.getLogger(__package__ + '.ProjectManager')

  def __init__(self):
    """Initializer of Project Manager

        Project **logging** & **configuration** will be initialized in this class
    """
    self.logger.info('Trying to load the configuration file...')
    self.config = ConfigManager()
    self.logger.info('Config Manager has been initiated using config file: ' + self.config.config_file_name)


  def install(self):
    """This function should be used to setup the Data Integrator on the current system

    .. warning::
        The current implementation will not check for existing installation and will override the
        exisiting settings if any exists
    """
    self.logger.info('Initiating the installation process for the Data Integrator')
    self.logger.info('Getting ready to ask setup questions')

    self.dbname = prompt('Database Name to be stored in config: ')
    self.dbtype = prompt('Database type: ')

    if self.dbtype == 'Oracle':
      self.dbhost = prompt('Hostname: ')
      self.dbport = prompt('Port: ')
      self.dbservice = prompt('Service: ')
      self.dbuser = prompt('Username: ')
      self.dbpassword =prompt('Password: ', is_password=True)
    # elif self.dbtype == 'OracleCX':
    #   self.dbtnsname = prompt('TNS Name: ')
    #   self.dbuser = prompt('Username: ')
    #   self.dbpassword = prompt('Password: ', is_password=True)
    # elif self.dbtype == 'SQLLiteFile':
    #   self.dbpathtofile = prompt('Filename including path: ')
    # elif self.dbtype == 'postgresql':
    #   self.dbhost = prompt('Hostname: ')
    #   self.dbservice = prompt('Service: ')
    #   self.dbuser = prompt('Username: ')
    #   self.dbpassword = prompt('Password: ', is_password=True)

    self.logger.info('Below database detalis will be stored in config file')
    self.logger.info('DB Name: ' + self.dbname + ' DB Type: ' + self.dbtype + ' DB Host: ' + self.dbhost + ' DB Port: ' + self.dbport)
    self.logger.info('DB Service: ' + self.dbservice + ' DB Username: ' + self.dbuser)

    if not self.config.config.has_section('Database'):
      self.config.add_section('Database')

    self.config.set('Database', 'DB_Name', self.dbname)
    self.config.set('Database', 'DB_Type', self.dbtype)
    self.config.set('Database', 'DB_Host', self.dbhost)
    self.config.set('Database', 'DB_Port', self.dbport)
    self.config.set('Database', 'DB_Service', self.dbservice)
    self.config.set('Database', 'DB_Username', self.dbuser)
    self.config.set('Database', 'DB_Password', self.dbpassword)

    self.metadatadbconnection = self._construct_db_uri()
    self.config.set('Database', 'Metadata_db_connection', self.metadatadbconnection)
    self.config.save()

    self.logger.info('Database details stored successfully!')


  def _connect_to_db(self):
    self.logger.info('Trying to connect to database "' + self.dbname + '"')



  def _construct_db_uri(self):
    switcher = {
      'Oracle': 'oracle://' + self.dbuser + ':' + self.dbpassword + '@' + self.dbhost + ':' + self.dbport + '/'+ self.dbservice
    }
    return switcher.get(self.dbtype, None)

if __name__ == '__main__':
  SetupManager().install()
