"""Module with abstract classes to work with action outcomes."""

from abc import ABC, abstractmethod


class Detail(ABC):
    """Class to manage a single detail of a consequence."""

    @abstractmethod
    def get_description(self):
        """Get description of the detail.

        :returns: description of the detail
        :rtype: str
        """

    @abstractmethod
    def get_image(self):
        """Get image identifier of the detail.

        :returns: a string value to identify an image of the detail
        :rtype: str
        """


class Consequence(ABC):
    """Class to manage a consequence of an action."""

    @abstractmethod
    def get_depiction(self):
        """Get depiction of the consequence.

        :returns: depiction of the consequence
        :rtype: :class:`Depiction <sunlessadventure.abstract.depiction.Depiction>`
        """

    @abstractmethod
    def get_details(self):
        """Get details of the consequence.

        :returns: list of individual entries that forms the consequence
        :rtype: iterable with instances of :class:`Detail`
        """

    @abstractmethod
    def get_resolution(self):
        """Get the text to describe the resolution of the consequence.

        :returns: text to describe the resolution of the consequence
        :rtype: str
        """


class Outcome(ABC):
    """Class to manage a outcome of an action."""

    @abstractmethod
    def get_consequences(self):
        """Get consequences.

        :returns: list of consequences
        :rtype: iterable with instances of :class:`Consequence`
        """

    @abstractmethod
    def get_target(self):
        """Get target location.

        :returns: identifier of the location to navigate to
        :rtype: str
        """
