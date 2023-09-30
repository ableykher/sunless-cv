"""Module to manage static depictions."""

from sunlessadventure.abstract.depiction import Depiction


class StaticDepiction(Depiction):
    """Class to describe an entity."""

    def __init__(self, title, description, image):
        self._title = str(title)
        self._description = str(description)
        self._image = str(image)

    def get_title(self):
        """Get title.

        :returns: short summary
        :rtype: str
        """
        return self._title

    def get_description(self):
        """Get description.

        :returns: long description
        :rtype: str
        """
        return self._description

    def get_image(self):
        """Get image identifier.

        :returns: a string value to identify an image
        :rtype: str
        """
        return self._image
