"""Module with classes to work with static locations."""

from sunlessadventure.abstract.location import Exit, Location


class StaticExit(Exit):
    """Class to manage a static exit from a location."""

    def __init__(self, name, target):
        self._name = str(name)
        self._target = str(target)

    def get_name(self):
        """Get name of the exit.

        :returns: name of the exit
        :rtype: str
        """
        return self._name

    def get_target(self):
        """Get target location.

        :returns: identifier of the location to navigate to
        :rtype: str
        """
        return self._target


class StaticLocation(Location):
    """Class to manage a static location."""

    def __init__(self, location_id, depiction, actions=(), exit_=None):
        self._id = str(location_id)
        self._depiction = depiction
        self._actions = tuple(actions)
        self._exit = exit_

    def visit(self):
        """Visit the location."""

    def get_id(self):
        """Get identifier of the location.

        :returns: identifier of the location
        :rtype: str
        """
        return self._id

    def get_depiction(self):
        """Get depiction of the location.

        :returns: depiction of the location
        :rtype: :class:`Depiction <sunlessadventure.abstract.depiction.Depiction>`
        """
        return self._depiction

    def get_actions(self):
        """Get actions available in the location.

        :returns: list of available actions
        :rtype: iterable with instances of :class:`Action <sunlessadventure.abstract.action.Action>`
        """
        return self._actions

    def get_exit(self):
        """Get exit.

        :returns: information about the exit from the location
        :rtype: :class:`Exit` or None, if there is no exit
        """
        return self._exit
