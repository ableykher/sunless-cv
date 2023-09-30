"""Module with abstract progress tracker."""

from abc import ABC, abstractmethod


class AbstractTracker(ABC):
    """Class for the abstract tracker."""

    @abstractmethod
    def get_progress_percentage(self):
        """Get current progress.

        :returns: progress percentage
        :rtype: float
        """

    @classmethod
    def __subclasshook__(cls, other):
        if cls is AbstractTracker:
            if any("get_progress_percentage" in parent.__dict__ for parent in other.__mro__):
                return True
        return NotImplemented
