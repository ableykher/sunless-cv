"""Module with a tracker for the watch status in Sunless CV."""

from sunlesscv.progress.abstract import AbstractTracker


class WatchTracker(AbstractTracker):
    """Class to track the watched tracker."""

    def __init__(self):
        super().__init__()
        self.__is_watched = False

    @property
    def is_watched(self):
        """Whether there is somebody watching."""
        return self.__is_watched

    @is_watched.setter
    def is_watched(self, value):
        """Whether there is somebody watching."""
        self.__is_watched = bool(value)

    def get_progress_percentage(self):
        """Get current progress.

        :returns: progress percentage
        :rtype: float
        """
        return 100 * int(self.__is_watched)
