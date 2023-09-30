"""Module with the location factory of Sunless CV."""

from sunlessadventure.abstract.location import (
    LocationFactory as AbstractLocationFactory,
    LocationError,
)

from sunlesscv.identifier import LocationId
from sunlesscv.location._story.home import create_home_location
from sunlesscv.location._story.maze import create_maze_location
from sunlesscv.location._story.hallway import create_hallway_location
from sunlesscv.location._story.profession import create_profession_location
from sunlesscv.location._story.technology import create_technology_location
from sunlesscv.location._story.company import create_company_location
from sunlesscv.location._story.personality import create_personality_location


class LocationFactory(AbstractLocationFactory):
    """Class to manager locations of Sunless CV."""

    def __init__(self, progress_manager):
        self._progress_manager = progress_manager
        self._locations = {}

    def get_location(self, location_id):
        """Get a location by its identifier.

        :param location_id: identifier of the location
        :type: str
        :returns: location
        :rtype: :class:`Location`
        :raises: :exc:`LocationError`
        """
        match location_id:
            case LocationId.HOME.value:
                location = self._get_home_location()
            case LocationId.MAZE.value:
                location = self._get_maze_location()
            case LocationId.HALLWAY.value:
                location = self._get_hallway_location()
            case LocationId.PROFESSION.value:
                location = self._get_profession_location()
            case LocationId.TECHNOLOGY.value:
                location = self._get_technology_location()
            case LocationId.COMPANY.value:
                location = self._get_company_location()
            case LocationId.PERSONALITY.value:
                location = self._get_personality_location()
            case _:
                raise LocationError(f"Unknown location '{location_id}'")

        return location

    def get_default_location_id(self):
        """Get the identifier of the default location.

        :returns: identifier of the default location
        :rtype: str
        """
        return LocationId.MAZE.value

    def _get_home_location(self):
        """Get home location.

        :returns: home location
        :rtype: :class:`Location`
        """
        if LocationId.HOME.value not in self._locations:
            self._locations[LocationId.HOME.value] = create_home_location(
                location_tracker=self._progress_manager.location_tracker,
                watch_tracker=self._progress_manager.watch_tracker,
            )

        return self._locations[LocationId.HOME.value]

    def _get_maze_location(self):
        """Get maze location.

        :returns: maze location
        :rtype: :class:`Location`
        """
        if LocationId.MAZE.value not in self._locations:
            self._locations[LocationId.MAZE.value] = create_maze_location(
                location_tracker=self._progress_manager.location_tracker,
                watch_tracker=self._progress_manager.watch_tracker,
            )

        return self._locations[LocationId.MAZE.value]

    def _get_hallway_location(self):
        """Get hallway location.

        :returns: hallway location
        :rtype: :class:`Location`
        """
        if LocationId.HALLWAY.value not in self._locations:
            self._locations[LocationId.HALLWAY.value] = create_hallway_location(
                location_tracker=self._progress_manager.location_tracker,
                watch_tracker=self._progress_manager.watch_tracker,
            )

        return self._locations[LocationId.HALLWAY.value]

    def _get_profession_location(self):
        """Get profession location.

        :returns: profession location
        :rtype: :class:`Location`
        """
        if LocationId.PROFESSION.value not in self._locations:
            self._locations[LocationId.PROFESSION.value] = create_profession_location(
                location_tracker=self._progress_manager.location_tracker,
                watch_tracker=self._progress_manager.watch_tracker,
            )

        return self._locations[LocationId.PROFESSION.value]

    def _get_technology_location(self):
        """Get technology location.

        :returns: technology location
        :rtype: :class:`Location`
        """
        if LocationId.TECHNOLOGY.value not in self._locations:
            self._locations[LocationId.TECHNOLOGY.value] = create_technology_location(
                location_tracker=self._progress_manager.location_tracker,
                watch_tracker=self._progress_manager.watch_tracker,
                competence_tracker=self._progress_manager.competence_tracker,
            )

        return self._locations[LocationId.TECHNOLOGY.value]

    def _get_company_location(self):
        """Get company location.

        :returns: company location
        :rtype: :class:`Location`
        """
        if LocationId.COMPANY.value not in self._locations:
            self._locations[LocationId.COMPANY.value] = create_company_location(
                location_tracker=self._progress_manager.location_tracker,
                watch_tracker=self._progress_manager.watch_tracker,
                competence_tracker=self._progress_manager.competence_tracker,
            )

        return self._locations[LocationId.COMPANY.value]

    def _get_personality_location(self):
        """Get personality location.

        :returns: personality location
        :rtype: :class:`Location`
        """
        if LocationId.PERSONALITY.value not in self._locations:
            self._locations[LocationId.PERSONALITY.value] = create_personality_location(
                self._progress_manager.location_tracker,
                self._progress_manager.watch_tracker,
                self._progress_manager.distrust_tracker,
            )

        return self._locations[LocationId.PERSONALITY.value]
