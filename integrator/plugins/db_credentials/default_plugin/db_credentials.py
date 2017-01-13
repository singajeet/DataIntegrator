"""
.. module:: db_credentials.default_plugin.db_credentials
        :platform: Unix, Windows
        :synopsis: module to load and store the db credentials used for node

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from integrator.node.interfaces import INodeDBCredentials
import os
from prompt_toolkit import prompt


class DefaultDBCredentials(INodeDBCredentials):
    """Default implementation for storing and loading the db credentials
    """

    _iplugin_name = 'DefaultDBCredentials'
    _iplugin_type = 'DatabaseCredentials'

    _db_credentials_file_name = '.default.db.credentials.store'
    _db_credentials_folder_path = os.path.expanduser('~') + \
        os.sep + '.data_integrator' + \
        os.sep + 'db_cred' + os.sep

    def credentials_exists(self):
        return os.path.isfile(self._db_credentials_folder_path + self._db_credentials_file_name)

    def prompt_credentials(self):
        self._user_name = prompt('Enter db username: ')
        self._password = prompt('Enter password: ', is_password=True)

    def save_credentials(self):
        with open(self._db_credentials_folder_path + self._db_credentials_file_path, 'w') as file:
            file.write('%s%s' % (self._user_name, os.linesep))
            file.write(self._password)

    def load_credentials(self):
        with open(self._db_credentials_folder_path + self._db_credentials_file_path, 'r') as file:
            self._user_name = file.readline()
            self._password = file.readline()

    def get_credentials(self):
        return (self._user_name, self._password)
