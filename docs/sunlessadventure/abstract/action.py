"""Module with abstract classes to work with actions."""

from abc import ABC, abstractmethod


class Action(ABC):
    """Class to manage an action."""

    @abstractmethod
    def get_name(self):
        """Get name of the action.

        :returns: name of the action
        :rtype: str
        """

    @abstractmethod
    def get_depiction(self):
        """Get depiction of the action.

        :returns: depiction of the action
        :rtype: :class:`Depiction <sunlessadventure.abstract.depiction.Depiction>`
        """

    @abstractmethod
    def perform(self):
        """Perform an action.

        :returns: outcome of the action
        :rtype: :class:`Outcome <sunlessadventure.abstract.outcome.Outcome>`
        """
