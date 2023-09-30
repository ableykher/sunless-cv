"""Module with the hallway location of Sunless CV."""

from sunlessadventure.core.depiction.static import StaticDepiction
from sunlessadventure.core.outcome.static import StaticDetail, StaticConsequence, StaticOutcome
from sunlessadventure.core.action.static import StaticAction
from sunlessadventure.core.location.static import StaticExit

from sunlesscv.identifier import LocationId
from sunlesscv.location.stable import StableLocation


def create_hallway_location(location_tracker, watch_tracker):
    """Get hallway location.

    :param location_tracker: a tracker of the locations of Sunless CV
    :type: :class:`LocationTracker <sunlesscv.progress.location.LocationTracker>`
    :param watch_tracker: a tracker of the watched status in Sunless CV
    :type: :class:`WatchTracker <sunlesscv.progress.watch.WatchTracker>`
    :returns: hallway location
    :rtype: :class:`StableLocation <sunlesscv.location.stable.StableLocation>`
    """
    return StableLocation(
        location_tracker=location_tracker,
        watch_tracker=watch_tracker,
        location_id=LocationId.HALLWAY.value,
        depiction=StaticDepiction(
            title="Hallway",
            description=(
                "Two doors face each other in a small hallway. "
                "Similar in size and color, they differ drastically in design."
            ),
            image="direction-signs.svg",
        ),
        actions=[
            StaticAction(
                name="Enter",
                depiction=StaticDepiction(
                    title="Work",
                    description=(
                        "The door is lightweight and does not have any locks. "
                        "You feel invited to peek inside and "
                        "find a spacious room like a studio or a workshop."
                    ),
                    image="gears.svg",
                ),
                outcome=StaticOutcome(target=LocationId.PROFESSION.value),
            ),
            StaticAction(
                name="Enter",
                depiction=StaticDepiction(
                    title="Life",
                    description=(
                        "The sturdy door is hardly moving under the weight of all the latches, "
                        "locks, and bolts. You have a feeling nobody is supposed to enter, and yet "
                        "someone left the door ajar. Was it for you? "
                        "You see a few personal items through the gap."
                    ),
                    image="charm.svg",
                ),
                outcome=StaticOutcome(
                    target=LocationId.PERSONALITY.value,
                    consequences=[
                        StaticConsequence(
                            depiction=StaticDepiction(
                                title="Hello?",
                                description=(
                                    "It is not clear if there is anybody in the room. "
                                    "Even though you see nobody, "
                                    "an eerie feeling emerges as you enter."
                                ),
                                image="walk.svg",
                            ),
                            resolution="Look around",
                            details=[
                                StaticDetail(
                                    description="Someone is watching you!",
                                    image="hidden.svg",
                                )
                            ],
                        ),
                    ],
                ),
            ),
        ],
        exit_=StaticExit(name="Exit", target=LocationId.HOME.value),
    )
