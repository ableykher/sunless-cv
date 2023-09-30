"""Module with abstract classes to depict entities."""

from abc import ABC, abstractmethod


class Depiction(ABC):
    """Class to describe an entity."""

    @abstractmethod
    def get_title(self):
        """Get title.

        :returns: short summary
        :rtype: str
        """

    @abstractmethod
    def get_description(self):
        """Get description.

        :returns: long description
        :rtype: str
        """

    @abstractmethod
    def get_image(self):
        """Get image identifier.

        :returns: a string value to identify an image
        :rtype: str
        """
