"""Module with abstract classes to work with locations."""

from abc import ABC, abstractmethod


class LocationError(Exception):
    """Exception during work with locations."""


class Exit(ABC):
    """Class to manage an exit from a location."""

    @abstractmethod
    def get_name(self):
        """Get name of the exit.

        :returns: name of the exit
        :rtype: str
        """

    @abstractmethod
    def get_target(self):
        """Get target location.

        :returns: identifier of the location to navigate to
        :rtype: str
        """


class Location(ABC):
    """Class to manage a location."""

    @abstractmethod
    def get_id(self):
        """Get identifier of the location.

        :returns: identifier of the location
        :rtype: str
        """

    @abstractmethod
    def visit(self):
        """Visit the location."""

    @abstractmethod
    def get_depiction(self):
        """Get depiction of the location.

        :returns: depiction of the location
        :rtype: :class:`Depiction <sunlessadventure.abstract.depiction.Depiction>`
        """

    @abstractmethod
    def get_actions(self):
        """Get actions available in the location.

        :returns: list of available actions
        :rtype: iterable with instances of :class:`Action <sunlessadventure.abstract.action.Action>`
        """

    @abstractmethod
    def get_exit(self):
        """Get exit.

        :returns: information about the exit from the location
        :rtype: :class:`Exit` or None, if there is no exit
        """


class LocationFactory(ABC):
    """Class to manage locations of an adventure."""

    @abstractmethod
    def get_location(self, location_id):
        """Get a location by its identifier.

        :param location_id: identifier of the location
        :type: str
        :returns: location
        :rtype: :class:`Location`
        :raises: :exc:`LocationError`
        """

    @abstractmethod
    def get_default_location_id(self):
        """Get the idetifier of the default location.

        :returns: identifier of the location
        :rtype: str
        """

    def get_default_location(self):
        """Get the default location.

        :returns: location
        :rtype: :class:`Location`
        """
        return self.get_location(location_id=self.get_default_location_id())
