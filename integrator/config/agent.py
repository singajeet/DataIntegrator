"""
.. module:: integrator.config.agent
        :platform: Unix, Windows
        :synopsis: Agent to communicate with the configuration server
                    and helps in get/set the configuration

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from integrator.core.interfaces.config_interface import IConfigurationAgent
from integrator.core.interfaces.agents import IAgentType
import logging
import redis
from flufl.i18n import initialize
import threading
import time
import sys


_ = initialize(__file__)

if sys.platform == 'win32':
    import multiprocessing.reduction

class RedisConfigurationAgent(IConfigurationAgent, threading.Thread):
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

    def __init__(self, host=None, port=None, password=None, key_domain='DI:CONFIG:COMMON'):
        self.logger.info(_('Starting configuration agent'))
        self._host = host
        self._port = port
        self._password = password
        self._redis_key_domain = key_domain

        try:
            self.logger.debug(_('Connecting to Redis server'))
            self._redis_server_object = redis.Redis(host=self._host)
                                                    # , port=self._port, password=self._password)
            self.logger.debug(_('Connected Successfully!'))
            self.start_server()
            self.logger.debug(_('Config agent has been started'))
            threading.Thread.__init__(self)
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
            print 'Sleeping...'
            time.sleep(10)

    def get(self, key):
        return self._c_dict[key]

    def set(self, key, value):
        if self._c_dict is None:
            self._c_dict = dict()
        self._c_dict[key] = value

    def start_server(self):
        self.logger.debug(_('Config dict manager created'))
        self._mutex = threading.Lock()
        self.logger.debug(_('Config dict manager server started'))

    def shutdown(self):
        self._terminate = True
        self._redis_server_object.save()
        self.logger.debug(_('Config dict manager server has been shutdown'))


"""
if __name__ == '__main__':
    test_server = RedisConfigurationAgent(host='localhost')
    test_server.start()
    test_server.set('testkey1', 'testvalue1')
    test_server.set('testkey2', 'testvalue2')

    print(test_server.get('testkey2'))
    print(test_server.get('testkey1'))

    test_server.shutdown()
"""







