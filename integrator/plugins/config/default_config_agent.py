"""
.. module:: integrator.config.default_config_agent
        :platform: Unix, Windows
        :synopsis: Agent to communicate with the configuration server
                    and helps in get/set the configuration

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
import integrator.core.interfaces.configuration_agent_plugins as interfaces
from integrator.core.interfaces.agents import IAgentType
import logging
import redis
from flufl.i18n import initialize
import threading
import time


_ = initialize(__file__)


class RedisConfigurationAgent(interfaces.IConfigurationAgent, threading.Thread):
    """Redis configuration agent implementation to save/load configuration
        on remote redis system
    """
    logger = logging.getLogger('%s.RedisConfigurationAgent' % __package__)

    _agent_name = 'RedisConfigurationAgent'
    _agent_type = IAgentType.REDIS
    _iplugin_name = 'RedisConfigurationAgentPlugin'

    _password = None
    _host = None
    _port = None

    _redis_key_domain = 'DI:CONFIG:COMMON'
    _redis_server_object = None
    _manager = None
    _c_dict = None
    _redis_process = None
    _terminate = False
    _refresh_freq = 10

    def __init__(self, **kwargs):
        self.logger.info(_('Starting configuration agent'))
        self._host = kwargs.get('host', None)
        self._port = kwargs.get('port', None)
        self._password = kwargs.get('password', None)
        self._redis_key_domain = kwargs.get('key_domain', 'DI:CONFIG:COMMON')
        self._refresh_freq = kwargs.get('refresh_freq', 10)

        try:
            self.logger.debug(_('Connecting to Redis server'))
            self._redis_server_object = redis.Redis(**kwargs)
            self.logger.debug(_('Connected Successfully!'))
            threading.Thread.__init__(self)

            self.start_server()

        except Exception as ex:
            self.logger.error(_('Error while starting RedisConfigAgent: %s') % ex.message)
            raise

    def run(self):
        """Dict will be refreshed from Redis
        """
        while not self._terminate:
            self._mutex.acquire()
            # save in-memory dict back to redis
            for nkey, nvalue in self._c_dict.items():
                self._redis_server_object.hmset(self._redis_key_domain, {nkey: nvalue})
            self._redis_server_object.save()
            self.logger.debug(_('local store saved to redis'))
            # load the key/value from redis into memory
            self._c_dict = self._redis_server_object.hgetall(self._redis_key_domain)
            self.logger.debug(_('local store refreshed from redis'))
            self._mutex.release()
            time.sleep(self._refresh_freq)

    def get(self, key):
        return self._c_dict[key]

    def set(self, key, value):
        self._c_dict[key] = value

    def start_server(self):
        if self._c_dict is None:
                self._c_dict = dict()
        self.logger.debug(_('local config store manager initialized'))
        self._mutex = threading.Lock()
        self.start()
        self.logger.info(_('Agent started for key domain: %s') % self._redis_key_domain)

    def stop_server(self):
        self._terminate = True
        self._redis_server_object.save()
        self.logger.debug(_('Config dict manager server has been stopped'))


"""if __name__ == '__main__':
    test_server = RedisConfigurationAgent(host='localhost')
    test_server.set('testkey1', 'testvalue1')
    test_server.set('testkey2', 'testvalue2')

    print(test_server.get('testkey2'))
    print(test_server.get('testkey1'))

    test_server.shutdown()"""
