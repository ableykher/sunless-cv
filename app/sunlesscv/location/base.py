"""Module with base class to work with locations of Sunless CV."""

from sunlessadventure.abstract.location import Location as AbstractLocation


class Location(AbstractLocation):
    """Class to manage a location of Sunless CV."""

    def __init__(self, location_tracker, watch_tracker, is_watched):
        super().__init__()
        self.__location_tracker = location_tracker
        self.__watch_tracker = watch_tracker
        self.__is_watched = bool(is_watched)

    def visit(self):
        """Visit the location."""
        self._location_tracker.visit(location_id=self.get_id())
        self._watch_tracker.is_watched = self.__is_watched

    @property
    def _location_tracker(self):
        """Location tracker."""
        return self.__location_tracker

    @property
    def _watch_tracker(self):
        """Watch tracker."""
        return self.__watch_tracker
