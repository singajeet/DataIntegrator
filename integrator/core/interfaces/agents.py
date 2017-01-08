"""
.. module:: integrator.core.interfaces.agents
        :platform: Unix, Windows
        :synopsis: Abstract interface for agents

.. moduleauthor:: Ajeet Singh <singajeet@gmail.com>
"""
import enum


class IAgent:
    """Abstract class for agents in DI
    """

    _agent_name = None
    _agent_type = None

    @property
    def agent_type(self):
        return self._agent_type

    @property
    def agent_name(self):
        return self._agent_name


class IAgentType(enum.Enum):
    """Defines all config agent supported by DI
    """
    REDIS = 1
    MEMCACHED = 2
    NOSQL = 3
