"""
.. module:: integrator.core.interfaces.config_interface
        :platform: Unix, Windows
        :synopsis: Interface to config agent which will be used get/set configuration

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
from yapsy.IPlugin import IPlugin
from flufl.i18n import initialize
from integrator.core.interfaces.agents import IAgent

_ = initialize(__file__)


class ConfigAgentNotImplementedError(Exception):
    """Exception to raise when no agent is defined
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class IConfigurationAgent(IPlugin, IAgent):
    """Abstract interface to configuration agent
        Each config agent should implement the below members
    """

    _iplugin_name = None

    @property
    def iplugin_name(self):
        return self._iplugin_name

    @iplugin_name.setter
    def iplugin_name(self, value):
        self._iplugin_name = value

    def refresh(self):
        raise ConfigAgentNotImplementedError(_('No ConfigAgent implemented'), _('This method needs to be implmented by an subclass'))

    def get(self, key):
        raise ConfigAgentNotImplementedError(_('No ConfigAgent implemented'), _('This method needs to be implmented by an subclass'))

    def set(self, key, value):
        raise ConfigAgentNotImplementedError(_('No ConfigAgent implemented'), _('This method needs to be implmented by an subclass'))
