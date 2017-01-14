"""
.. module:: integrator.node.interfaces
        :platform: Unix, Windows
        :synopsis: Abstract decleration of an node in distributed system

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from integrator.log.logger import create_logger
from integrator.node.interfaces import INodeDatabaseManager, INodeDatabaseType, Base, INodeModel
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flufl.i18n import initialize


_ = initialize(__file__)


class DefaultNodeDatabaseManager(INodeDatabaseManager):
    """
    """

    _iplugin_name = 'DefaultNodeDatabase'
    _iplugin_type = 'NodeDatabase'
    _database_name = 'db.node.sqlite'
    _database_type = INodeDatabaseType.SQLITE
    _db_file_name = 'db.node.sqlite'
    _db_file_path = ('%s%s.data_integrator%sdb%s' % (os.path.expanduser('~'), os.sep, os.sep, os.sep))
    _db_engine = None

    def __init__(self, username, password):
        """
        """
        self.logger = create_logger('%s.DefaultNodeDatabaseManager' % (__name__))

    def node_db_exists(self):
        """
        """
        self.logger.debug(_('Searching database at: %s') % self._db_file_path)
        return os.path.isfile(self._db_file_path + self._db_file_name)

    def load_db_details(self):
        """
        """
        pass

    def open_or_create_database(self):
        """
        """
        try:
            if not os.path.isdir(self._db_file_path):
                os.mkdir(self._db_file_path)
                self.logger.debug(_('database path created: %s') % self._db_file_path)

            self._db_engine = create_engine('sqlite:///%s%s' % (self._db_file_path, self._db_file_name))
            Base.metadata.create_all(self._db_engine)
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
            query = session.query(INodeModel).filter(INodeModel.sys_identifier == node.sys_identifier)
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
            self.logger.debug(_('Node information already exist in db'))
            query = session.query(INodeModel).filter(INodeModel.sys_identifier == node.sys_identifier)
            query.first()
            query.delete()
            session.add(node)
            session.commit()
            self.logger.debug(_('Updated node information saved in db'))
        except Exception as ex:
            self.logger.error(_('Unable to update node information in db: %s') % (ex.message))

    def node_details_exists(self, sys_id):
        """
        """
        session = self.Session()
        query = session.query(INodeModel).filter(INodeModel.sys_identifier == sys_id)
        return True if query.count() > 0 else False

    def load_node_details(self, sys_id):
        """
        """
        session = self.Session()
        node = session.query(INodeModel).filter(INodeModel.sys_identifier == sys_id)
        return node

    def validate_node_details(self, v_sys_id):
        pass
