"""
.. module:: integrator.config.agent
        :platform: Unix, Windows
        :synopsis: Agent to communicate with the configuration server
                    and helps in get/set the configuration

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from integrator.core.interfaces.config_interface import IConfigurationAgent, ConfigAgentType
import logging
import redis
from flufl.i18n import initialize
from multiprocessing import Process, Manager


_ = initialize(__file__)


class RedisConfigurationAgent(IConfigurationAgent):
    """Redis configuration agent implementation to save/load configuration
        on remote redis system
    """
    logger = logging.getLogger('%s.RedisConfigurationAgent' % __package__)

    _agent_name = 'RedisConfigurationAgent'
    _agent_type = ConfigAgentType.REDIS
    _iplugin_name = 'RedisConfigurationAgentPlugin'

    _password = None
    _host = None
    _port = None

    _redis_key_domain = 'DI:CONFIG:COMMON:'
    _redis_server_object = None

    def __init__(self, host=None, port=None, password=None):
        self.logger.info(_('Starting configuration agent'))
        self._host = host
        self._port = port
        self._password = password

        try:
            self.logger.debug(_('Connecting to Redis server'))
            self._redis_server_object = redis.Redis(host=self._host, port=self._port, password=self._password)
            self.logger.debug(_('Connected Successfully!'))
            self.start_server()
        except Exception as ex:
            self.logger.error(_('Error while starting RedisConfigAgent: %s') % ex.message)
            raise

    def refresh(self, p_dict):
        """Dict will be refreshed from Redis
        """
        pass

    def start_server(self):
        self._manager = Manager()
        self._p_dict = self._manager.dict()
        self._redis_process = Process(target=self.refresh, args=(self._p_dict))
        self._redis_process.start()












