"""Module to manage static outcomes."""

from sunlessadventure.abstract.outcome import Detail, Consequence, Outcome


class StaticDetail(Detail):
    """Class to manage a single static detail of a consequence."""

    def __init__(self, description, image):
        self._description = str(description)
        self._image = str(image)

    def get_description(self):
        """Get description of the detail.

        :returns: description of the detail
        :rtype: str
        """
        return self._description

    def get_image(self):
        """Get image identifier of the detail.

        :returns: a string value to identify an image of the detail
        :rtype: str
        """
        return self._image


class StaticConsequence(Consequence):
    """Class to manage a consequence of an action."""

    def __init__(self, depiction, resolution, details=()):
        self._depiction = depiction
        self._resolution = str(resolution)
        self._details = tuple(details)

    def get_depiction(self):
        """Get depiction of the consequence.

        :returns: depiction of the consequence
        :rtype: :class:`Depiction <sunlessadventure.abstract.depiction.Depiction>`
        """
        return self._depiction

    def get_details(self):
        """Get details of the consequence.

        :returns: list of individual entries that forms the consequence
        :rtype: iterable with instances of :class:`Detail`
        """
        return self._details

    def get_resolution(self):
        """Get the text to describe the resolution of the consequence.

        :returns: text to describe the resolution of the consequence
        :rtype: str
        """
        return self._resolution


class StaticOutcome(Outcome):
    """Class to manage a static outcome of an action."""

    def __init__(self, target, consequences=()):
        self._target = str(target)
        self._consequences = tuple(consequences)

    def get_consequences(self):
        """Get consequences.

        :returns: list of consequences
        :rtype: iterable with instances of :class:`Consequence`
        """
        return self._consequences

    def get_target(self):
        """Get target location.

        :returns: identifier of the location to navigate to
        :rtype: str
        """
        return self._target
