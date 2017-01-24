import integrator.core.interfaces.network as interface
from yapsy.PluginManager import PluginManager
from twisted.internet import reactor
from integrator.log.logger import create_logger
from twisted.logger import Logger

logger = create_logger(__name__)
#ylogger = create_logger('yapsy')
tlogger = Logger(__name__)

def run():

    pmanager = PluginManager(categories_filter={'BroadcastService': interface.INetworkService})
    pmanager.setPluginPlaces(['./integrator/plugins'])
    pmanager.collectPlugins()

    broadcast_service = pmanager.getPluginByName('NodeBroadcasterService', category='BroadcastService').plugin_object

    reactor.listenUDP(9999, broadcast_service.getNodeBroadcastProtocol())
    logger.debug('Listenning on port 9999')
    reactor.run()


if __name__ == '__main__':
    run()
