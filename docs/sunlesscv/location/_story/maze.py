"""Module with the maze location of Sunless CV."""

from sunlessadventure.core.depiction.static import StaticDepiction
from sunlessadventure.core.outcome.static import StaticConsequence, StaticOutcome
from sunlessadventure.core.action.static import StaticAction

from sunlesscv.identifier import LocationId
from sunlesscv.location.stable import StableLocation


def create_maze_location(location_tracker, watch_tracker):
    """Get maze location.

    :param location_tracker: a tracker of the locations of Sunless CV
    :type: :class:`LocationTracker <sunlesscv.progress.location.LocationTracker>`
    :param watch_tracker: a tracker of the watched status in Sunless CV
    :type: :class:`WatchTracker <sunlesscv.progress.watch.WatchTracker>`
    :returns: maze location
    :rtype: :class:`StableLocation <sunlesscv.location.stable.StableLocation>`
    """
    return StableLocation(
        location_tracker=location_tracker,
        watch_tracker=watch_tracker,
        location_id=LocationId.MAZE.value,
        depiction=StaticDepiction(
            title="Maze",
            description="You find yourself in a maze. How did you get here?",
            image="maze.svg",
        ),
        actions=[
            StaticAction(
                name="Explore",
                depiction=StaticDepiction(
                    title="Explore the maze",
                    description="This maze seems extraordinary. Perhaps it is worth exploring?",
                    image="tron-arrow.svg",
                ),
                outcome=StaticOutcome(
                    target=LocationId.MAZE.value,
                    consequences=[
                        StaticConsequence(
                            depiction=StaticDepiction(
                                title="Another room",
                                description=(
                                    "You entered another room in the maze, "
                                    "though it does not look different."
                                ),
                                image="tron-arrow.svg",
                            ),
                            resolution="Look around",
                        ),
                    ],
                ),
            ),
            StaticAction(
                name="Follow footprints",
                depiction=StaticDepiction(
                    title="Try to escape",
                    description=(
                        "There are subtle footprints on the ground. "
                        "They might lead to the exit."
                    ),
                    image="footsteps.svg",
                ),
                outcome=StaticOutcome(
                    target=LocationId.HOME.value,
                    consequences=[
                        StaticConsequence(
                            depiction=StaticDepiction(
                                title="Relief",
                                description=(
                                    "Luckily, after passing several rooms through, "
                                    "you find a ladder and can finally leave this maze."
                                ),
                                image="ladder.svg",
                            ),
                            resolution="Climb",
                        ),
                    ],
                ),
            ),
        ],
    )
