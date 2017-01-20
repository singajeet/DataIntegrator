"""
.. module:: db_credentials.default_plugin.db_credentials
        :platform: Unix, Windows
        :synopsis: module to load and store the db credentials used for node

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from integrator.log.logger import create_logger
import integrator.core.interfaces.node as interfaces
import sys
import os
from prompt_toolkit import prompt
from flufl.i18n import initialize
import keyring


_ = initialize(__file__)


class DefaultNodeAuthProvider(interfaces.INodeAuthProvider):
    """Default implementation for storing and loading the db credentials
    """

    _iplugin_name = 'DefaultNodeAuthProvider'
    _iplugin_type = 'AuthProvider'
    _user_id_file_path = ('%s%s.data_integrator%sdb_auth%s' % (os.path.expanduser('~'), os.sep, os.sep, os.sep))
    _user_id_file_name = '.node.user.id.store'
    _type = interfaces.AuthProviderType.GENERIC.value

    def __init__(self):
        """
        """
        self.logger = create_logger('%s.DefaultNodeAuthProvider' % (__name__))

    def set_type(self, auth_type):
        self._type = auth_type.value

    def credentials_exists(self):
        """
        """
        if os.path.isfile('%s%s' % (self._user_id_file_path, self._user_id_file_name)):
            return True
        else:
            return False

    def prompt_credentials(self):
        self._user_name = prompt(_('Enter username: '))
        self._password = prompt(_('Enter password: '), is_password=True)
        return (self._user_name, self._password)

    def save_credentials(self):
        try:
            self.logger.debug(_('Saving username in default auth store'))
            with open('%s%s' % (self._user_id_file_path, self._user_id_file_name), 'w') as file:
                file.write(self._user_name)
            self.logger.debug(_('Credentials saved to the default keyring vault'))
            keyring.set_password(self._type, self._user_name, self._password)
        except Exception as ex:
            self.logger.error(_('Unable to save db credentials: %s') % ex.message)
            sys.exit(1)

    def load_credentials(self):
        try:
            self.logger.debug(_('Reading username from default auth store'))
            with open('%s%s' % (self._user_id_file_path, self._user_id_file_name), 'r') as file:
                self._user_name = file.read()
            self.logger.debug(_('Reading credentials from default keyring vault'))
            keyring.get_password(self._type, self._user_name)
        except Exception as ex:
            self.logger.error(_('Unable to load db credentials: %s') % ex.message)
            sys.exit(1)

    def get_credentials(self):
        return (self._user_name, self._password)
