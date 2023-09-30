"""Module with a tracker for the distrust status in Sunless CV."""

from sunlesscv.progress.abstract import AbstractTracker


class DistrustTracker(AbstractTracker):
    """Class to track the distrust tracker."""

    def __init__(self):
        super().__init__()
        self.__is_distrusted = False

    @property
    def is_distrusted(self):
        """Whether distrust has emerged."""
        return self.__is_distrusted

    @is_distrusted.setter
    def is_distrusted(self, value):
        """Whether distrust has emerged."""
        self.__is_distrusted = bool(value)

    def get_progress_percentage(self):
        """Get current progress.

        :returns: progress percentage
        :rtype: float
        """
        return 100 * int(self.__is_distrusted)
