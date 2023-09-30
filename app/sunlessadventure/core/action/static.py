"""Module with classes to work with static actions."""

from sunlessadventure.abstract.action import Action


class StaticAction(Action):
    """Class to manage a static action."""

    def __init__(self, name, depiction, outcome):
        self._name = str(name)
        self._depiction = depiction
        self._outcome = outcome

    def get_name(self):
        """Get name of the action.

        :returns: name of the action
        :rtype: str
        """
        return self._name

    def get_depiction(self):
        """Get depiction of the action.

        :returns: depiction of the action
        :rtype: :class:`Depiction <sunlessadventure.abstract.depiction.Depiction>`
        """
        return self._depiction

    def perform(self):
        """Perform an action.

        :returns: outcome of the action
        :rtype: :class:`Outcome <sunlessadventure.abstract.outcome.Outcome>`
        """
        return self._outcome
