"""Module with stable locations of Sunless CV."""

from sunlesscv.location.base import Location


class StableLocation(Location):
    """Class to manage a stable location of Sunless CV."""

    def __init__(
            self,
            location_tracker,
            watch_tracker,
            location_id,
            depiction,
            actions=(),
            exit_=None,
        ):
        # pylint: disable=too-many-arguments
        super().__init__(
            location_tracker=location_tracker,
            watch_tracker=watch_tracker,
            is_watched=False,
        )
        self._id = str(location_id)
        self._depiction = depiction
        self._actions = tuple(actions)
        self._exit = exit_

    def get_id(self):
        """Get identifier of the location.

        :returns: identifier of the location
        :rtype: str
        """
        return self._id

    def get_depiction(self):
        """Get depiction of the location.

        :returns: depiction of the location
        :rtype: :class:`Depiction`
        """
        return self._depiction

    def get_actions(self):
        """Get actions available in the location.

        :returns: list of available actions
        :rtype: iterable with instances of :class:`Action`
        """
        return self._actions

    def get_exit(self):
        """Get exit.

        :returns: information about the exit from the location
        :rtype: :class:`Exit` or None, if there is no exit
        """
        return self._exit
