"""
.. module:: db_credentials.default_plugin.db_credentials
        :platform: Unix, Windows
        :synopsis: module to load and store the db credentials used for node

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from integrator.log.logger import create_logger
import integrator.node.interfaces as interfaces
import os
import sys
from prompt_toolkit import prompt
from flufl.i18n import initialize


_ = initialize(__file__)


class DefaultNodeDBAuthProvider(interfaces.INodeDBAuthProvider):
    """Default implementation for storing and loading the db credentials
    """

    _iplugin_name = 'DefaultDBCredentials'
    _iplugin_type = 'DatabaseCredentials'

    _db_credentials_file_name = '.default.db.credentials.store'
    _db_credentials_folder_path = ('%s%s.data_integrator%sdb_cred%s' % (os.path.expanduser('~'), os.sep, os.sep, os.sep))

    def __init__(self, file_name='.default.db.credentials.store'):
        """
        """
        self.logger = create_logger('%s.DefaultDBCredentials' % (__name__))
        self._db_credentials_file_name = file_name

    def credentials_exists(self):
        self.logger.debug(_('Searching db credentials at: %s') % self._db_credentials_folder_path)
        return os.path.isfile(self._db_credentials_folder_path + self._db_credentials_file_name)

    def prompt_credentials(self):
        self._user_name = prompt(_('Enter db username: '))
        self._password = prompt(_('Enter password: '), is_password=True)
        return (self._user_name, self._password)

    def save_credentials(self):
        try:
            if not os.path.isdir(self._db_credentials_folder_path):
                os.mkdir(self._db_credentials_folder_path)

            with open(self._db_credentials_folder_path + self._db_credentials_file_name, 'w') as file:
                file.write('%s%s' % (self._user_name, os.linesep))
                file.write(self._password)
        except Exception as ex:
            self.logger.error(_('Unable to save db credentials: %s') % ex.message)
            sys.exit(1)

    def load_credentials(self):
        try:
            with open(self._db_credentials_folder_path + self._db_credentials_file_name, 'r') as file:
                self._user_name = file.readline()
                self._password = file.readline()
        except Exception as ex:
            self.logger.error(_('Unable to load db credentials: %s') % ex.message)
            sys.exit(1)

    def get_credentials(self):
        return (self._user_name, self._password)
