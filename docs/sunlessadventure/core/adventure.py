"""Module to manage the status of an adventure."""

from sunlessadventure.abstract.location import LocationError


class AdventureError(Exception):
    """Exception raised during the adventure."""


class AdventureStateError(Exception):
    """Exception raised when an operation is blocked due to the state of an adventure."""


class Adventure:
    """Class to manage an adventure."""

    def __init__(self, location_factory, start_location_id):
        self._location_factory = location_factory

        try:
            location = location_factory.get_location(start_location_id)
        except LocationError:
            location = location_factory.get_default_location()
        location.visit()
        self.__location = location

        self._outcome = None
        self._consequence_index = 0

    def describe_location(self):
        """Describe the current location.

        :returns: a structured description of the current location
        :rtype: dict
        :raises: :exc:`AdventureStateError` if the location can't be described at the moment. For
            instance, if there is an unresolved consequence
        """
        if self._consequence is not None:
            raise AdventureStateError("There is an unresolved consequence")

        location = self._location
        location_depiction = location.get_depiction()

        actions = location.get_actions()
        described_actions = []
        for action in actions:
            action_depiction = action.get_depiction()
            described_actions.append({
                "depiction": {
                    "image": action_depiction.get_image(),
                    "title": action_depiction.get_title(),
                    "description": action_depiction.get_description(),
                },
                "name": action.get_name(),
            })

        exit_ = location.get_exit()
        described_exit = None
        if exit_ is not None:
            described_exit = exit_.get_name()

        return {
            "id": location.get_id(),
            "depiction": {
                "image": location_depiction.get_image(),
                "title": location_depiction.get_title(),
                "description": location_depiction.get_description(),
            },
            "actions": described_actions,
            "exit": described_exit,
        }

    def describe_consequence(self):
        """Describe the current consequence.

        :returns: a structured description of the current consequence
        :rtype: dict
        :raises: :exc:`AdventureStateError` if the consequence can't be described at the moment. For
            instance, if there is no consequence
        """
        consequence = self._consequence
        if consequence is None:
            raise AdventureStateError("There is no consequence")

        consequence_depiction = consequence.get_depiction()

        details = consequence.get_details()
        described_details = []
        for detail in details:
            described_details.append({
                "image": detail.get_image(),
                "description": detail.get_description(),
            })

        return {
            "depiction": {
                "image": consequence_depiction.get_image(),
                "title": consequence_depiction.get_title(),
                "description": consequence_depiction.get_description(),
            },
            "details": described_details,
            "resolution": consequence.get_resolution(),
        }

    def leave_location(self):
        """Leave the current location.

        :raises: :exc:`AdventureStateError` if the location can't be left. For instance, if
            there is an unresolved consequence or there is no exit.
        """
        if self._consequence is not None:
            raise AdventureStateError("There is an unresolved consequence")

        exit_ = self._location.get_exit()
        if exit_ is None:
            raise AdventureStateError("There is no exit")

        self._change_location(location_id=exit_.get_target())

    def perform_action(self, action_index):
        """Perform an action.

        :param action_index: index of the action
        :type: int
        :raises: :exc:`AdventureStateError` if the action can't be performed. For instance, if
            there is an unresolved consequence.
        """
        if self._consequence is not None:
            raise AdventureStateError("There is an unresolved consequence")

        try:
            action = self._location.get_actions()[action_index]
        except IndexError as error:
            raise AdventureStateError(
                f"There is no action at the position '{action_index}'",
            ) from error

        outcome = action.perform()
        if outcome.get_consequences():
            self._outcome = outcome
            self._consequence_index = 0
        else:
            self._change_location(location_id=outcome.get_target())

    def resolve_consequence(self):
        """Resolve the active consequence.

        :raises: :exc:`AdventureStateError` if the consequence can't be resolved at the moment. For
            instance, if there is no consequence
        """
        consequence = self._consequence
        if consequence is None:
            raise AdventureStateError("There is no consequence")

        self._consequence_index += 1

        outcome = self._outcome
        if outcome is not None and self._consequence_index >= len(outcome.get_consequences()):
            self._change_location(location_id=outcome.get_target())

    @property
    def _location(self):
        """Current location."""
        return self.__location

    @property
    def _consequence(self):
        """Get current consequence."""
        if self._outcome is None:
            return None

        consequences = self._outcome.get_consequences()
        if self._consequence_index >= len(consequences):
            return None

        return consequences[self._consequence_index]

    def _change_location(self, location_id):
        """Change the current location.

        :param location_id: identifier of the new location
        :type location_id: str
        """
        try:
            location = self._location_factory.get_location(location_id)
        except LocationError:
            location = self._location_factory.get_default_location()
        location.visit()

        self.__location = location
        self._outcome = None
        self._consequence_index = 0
