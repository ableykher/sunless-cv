"""Module to manage multiple trackers."""


class ProgressManager:
    """Class to manage different types of progress in the adventure."""

    def __init__(self, location_tracker, competence_tracker, distrust_tracker, watch_tracker):
        self._location_tracker = location_tracker
        self._competence_tracker = competence_tracker
        self._distrust_tracker = distrust_tracker
        self._watch_tracker = watch_tracker

    @property
    def location_tracker(self):
        """Location tracker."""
        return self._location_tracker

    @property
    def competence_tracker(self):
        """Competence tracker."""
        return self._competence_tracker

    @property
    def distrust_tracker(self):
        """Distrust tracker."""
        return self._distrust_tracker

    @property
    def watch_tracker(self):
        """Watch tracker."""
        return self._watch_tracker
