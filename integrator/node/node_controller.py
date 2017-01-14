"""
.. module:: integrator.node.node_controller
        :platform: Unix, Windows
        :synopsis: Abstract decleration of an node in distributed system

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from __future__ import unicode_literals
from integrator.log.logger import create_logger
from integrator.plugins.db_credentials.default_plugin.db_credentials import DefaultDBCredentials
from integrator.plugins.node.default_plugin.node import Node
from integrator.plugins.node_db.default_plugin.node_db_manager import DefaultNodeDatabaseManager
import sys
from flufl.i18n import initialize


_ = initialize(__file__)
# logger = logging.getLogger(__package__)
# logger.setLevel(logging.DEBUG)
# ch = logging.StreamHandler()
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# ch.setFormatter(formatter)
# logger.addHandler(ch)
logger = create_logger(__package__)


if __name__ == '__main__':
    logger.info(_('Data Integrator node has been started...'))
    node = Node()
    node.load_system_details()
    logger.debug(_('System details loaded'))
    logger.debug(node.node_details)

    v_sys_id = node.sys_id_exists()
    if v_sys_id == -1:
        logger.info(_('No existing configuration found. Building & configuring new node'))
        v_sys_id = node.create_node()
        logger.debug(_('Unique id generated for this node'))
    else:
        logger.info(_('Configuration found and will be checked for integrity'))

    if not node.validate_sys_id(v_sys_id):
        logger.error(_('Integrity check failed! System will exit now'))
        sys.exit(1)

    db_cred = DefaultDBCredentials()
    logger.debug(_('Loading db credentials'))
    (user, password) = (None, None)
    if not db_cred.credentials_exists():
        logger.debug(_('No db credentials found, user will be prompted for same'))
        (user, password) = db_cred.prompt_credentials()
        logger.debug(_('New db credentials: %s | %s') % (user, password))
        db_cred.save_credentials()
        logger.debug(_('db credentials saved successfully'))
    else:
        logger.debug(_('db credentials located and will be loaded'))
        db_cred.load_credentials()
        (user, password) = db_cred.get_credentials()
        logger.debug(_('Credentials loaded successfully: %s %s') % (user, password))

    db_manager = DefaultNodeDatabaseManager(user, password)
    logger.info(_('Node\'s database manager has been started'))
    if not db_manager.node_db_exists():
        logger.debug(_('Database is not configured yet and will be initiated now'))
        db_manager.create_database()
        logger.debug(_('Database configured successfully!'))







