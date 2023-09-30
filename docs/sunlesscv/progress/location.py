"""Module with a progress tracker for the locations of Sunless CV."""

from sunlesscv.identifier import LocationId
from sunlesscv.progress.abstract import AbstractTracker


class LocationTracker(AbstractTracker):
    """Class to track visited locations."""

    def __init__(self, valid_location_ids=None):
        super().__init__()
        self._visited_location_ids = set()

        if valid_location_ids is None:
            valid_location_ids = set(location_id.value for location_id in LocationId)
        self._valid_location_ids = frozenset(str(location_id) for location_id in valid_location_ids)

    def visit(self, location_id):
        """Mark a location as visited.

        :param location_id: identifier of the location
        :type: str
        """
        location_id = str(location_id)
        if location_id in self._valid_location_ids:
            self._visited_location_ids.add(location_id)

    def get_progress_percentage(self):
        """Get current progress.

        :returns: progress percentage
        :rtype: float
        """
        total = len(self._valid_location_ids)

        if total == 0:
            return 0

        return 100 * len(self._visited_location_ids) / total
