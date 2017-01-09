"""
.. module:: integrator.startup
        :platform: Unix, Windows
        :synopsis: Contains the logger and config classes for launching the app

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
import ConfigParser
import logging


class ConfigManager:
    """Reads the initial configuration to launch the app
    """

    def __init__(self):
        self.config_file_name = 'integrator/launcher/configuration.cfg'
        self.config = ConfigParser.ConfigParser()
        self.config.read(self.config_file_name)

    def get(self, section, key):
        return self.config.get(section, key, 0)

    def set(self, section, key, value):
        self.config.set(section, key, value)

    def save(self):
        with open(self.config_file_name, 'wb') as config_file:
            self.config.write(config_file)


class Logger:
    """Logger to use during app launch
    """
    def __init__(self):
        self._logger = logging.getLogger('DataIntegrator.launcher')
        self._logger.setLevel(logging.INFO)

        # Logs will be written to the below log file
        self._file_handler = logging.FileHandler('launcher.log')
        self._file_handler.setLevel(logging.INFO)

        # Logs will be sent to console terminal also
        self._console_handler = logging.StreamHandler()
        self._console_handler.setLevel(logging.INFO)

        # Log formatter
        self._formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self._file_handler.setFormatter(self._formatter)
        self._console_handler.setFormatter(self._formatter)

        self._logger.addHandler(self._file_handler)
        self._logger.addHandler(self._console_handler)

    def debug(self, message):
        self._logger.debug(message)

    def info(self, message):
        self._logger.info(message)

    def warn(self, message):
        self._logger.warn(message)

    def error(self, message):
        self._logger.error(message)

    def critical(self, message):
        self._logger.critical(message)


def launch():
    """create instance of launcher logger and config to start the app
    """

    ################ start the launcher logger ###########################
    launch_log = Logger()
    launch_log.info('Starting the DATA INTEGRATOR application')
    launch_log.info('Server will be booted as per the role assigned')
    launch_log.info('Services will be started as per the role')

    ################ start the launcher config manager ###################
    launch_log.debug('Creating the launcher config manager')
    launch_config = ConfigManager()
    launch_log.info('Launcher configuration loaded from: %s' % launch_config.config_file_name)

    ########### start the config agent to connect with central config server ##############
    config_server_host = launch_config.get('configuration', 'config_server_host')
    config_server_port = launch_config.get('configuration', 'config_server_port')
    config_server_password = launch_config.get('configuration', 'config_server_password')







