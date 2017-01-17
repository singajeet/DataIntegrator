"""
.. module:: integrator.node.interfaces
        :platform: Unix, Windows
        :synopsis: Abstract decleration of an node in distributed system

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from integrator.log.logger import create_logger
import integrator.node.interfaces as interfaces
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flufl.i18n import initialize


_ = initialize(__file__)


class DefaultNodeDatabaseManager(interfaces.INodeDatabaseManager):
    """
    """

    _iplugin_name = 'DefaultNodeDatabase'
    _iplugin_type = 'NodeDatabase'
    _database_name = 'db.node.sqlite'
    _database_type = interfaces.INodeDatabaseType.SQLITE
    _db_file_name = 'db.node.sqlite'
    _db_file_path = ('%s%s.data_integrator%sdb%s' % (os.path.expanduser('~'), os.sep, os.sep, os.sep))
    _db_engine = None

    def __init__(self):
        """
        """
        self.logger = create_logger('%s.DefaultNodeDatabaseManager' % (__name__))

    def node_db_exists(self):
        """
        """
        self.logger.debug(_('Searching database at: %s') % self._db_file_path)
        return os.path.isfile(self._db_file_path + self._db_file_name)

    def prepare_node_session(self, dbcredentials):
        """
        """
        pass

    def open_or_create_database(self):
        """
        """
        try:
            if not os.path.isdir(self._db_file_path):
                os.mkdir(self._db_file_path)
                self.logger.debug(_('database path set to: %s') % self._db_file_path)

            self._db_engine = create_engine('sqlite:///%s%s' % (self._db_file_path, self._db_file_name))
            interfaces.Base.metadata.create_all(self._db_engine)
            self.Session = sessionmaker(bind=self._db_engine)
            self.logger.debug(_('Sqlite database engine created successfully'))
        except Exception as ex:
            self.logger.error(_('Unable to create database engine:%s %s') % (ex, ex.message))
            sys.exit(1)

    def save_node_details(self, node):
        """
        """
        try:
            session = self.Session()
            self.logger.debug(_('Session established with database'))
            query = session.query(interfaces.INodeModel).filter(interfaces.INodeModel.sys_identifier == node.sys_identifier)
            if query.count() == 0:
                self.logger.debug(_('No record exist for node'))
                session.add(node)
                session.commit()
                self.logger.debug(_('New node saved in database'))
            else:
                self.logger.warn(_('Node details already exists and can\'t be overwritten'))
        except Exception as ex:
            self.logger.error(_('Unable to save node information in db: %s') % (ex.message))

    def update_node_details(self, node):
        """
        """
        try:
            session = self.Session()
            self.logger.debug(_('Node information already exist in database'))
            query = session.query(interfaces.INodeModel).filter(interfaces.INodeModel.sys_identifier == node.sys_identifier)
            query.first()
            query.delete()
            session.add(node)
            session.commit()
            self.logger.debug(_('Node details updated in database'))
        except Exception as ex:
            self.logger.error(_('Unable to update node information in db: %s') % (ex.message))

    def node_details_exists(self, sys_id):
        """
        """
        session = self.Session()
        node = session.query(interfaces.INodeModel).filter(interfaces.INodeModel.sys_identifier == sys_id)
        return True if node.count() > 0 else False

    def load_node_details(self, sys_id):
        """
        """
        try:
            session = self.Session()
            node = session.query(interfaces.INodeModel).filter(interfaces.INodeModel.sys_identifier == sys_id)
            self.logger.debug(_('Node details have been loaded from database'))
            return node
        except Exception as ex:
            self.logger.error(_('Unable to load database details from database: %s' % ex.message))
