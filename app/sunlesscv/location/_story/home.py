"""Module with the home location of Sunless CV."""

from sunlessadventure.core.depiction.static import StaticDepiction
from sunlessadventure.core.outcome.static import StaticDetail, StaticConsequence, StaticOutcome
from sunlessadventure.core.action.static import StaticAction

from sunlesscv.identifier import LocationId
from sunlesscv.location.stable import StableLocation


def create_home_location(location_tracker, watch_tracker):
    """Get home location.

    :param location_tracker: a tracker of the locations of Sunless CV
    :type: :class:`LocationTracker <sunlesscv.progress.location.LocationTracker>`
    :param watch_tracker: a tracker of the watched status in Sunless CV
    :type: :class:`WatchTracker <sunlesscv.progress.watch.WatchTracker>`
    :returns: home location
    :rtype: :class:`StableLocation <sunlesscv.location.stable.StableLocation>`
    """
    return StableLocation(
        location_tracker=location_tracker,
        watch_tracker=watch_tracker,
        location_id=LocationId.HOME.value,
        depiction=StaticDepiction(
            title="Adventure",
            description=(
                "You know his name but have never met him. You have got an address to learn more. "
                "What can this place tell you about Andrew Bleykher?"
            ),
            image="treasure-map.svg",
        ),
        actions=(
            StaticAction(
                name="Enter",
                depiction=StaticDepiction(
                    title="Let me in!",
                    description=(
                        "You are determined to investigate and do not want to lose any time."
                    ),
                    image="open-gate.svg",
                ),
                outcome=StaticOutcome(target=LocationId.HALLWAY.value),
            ),
            StaticAction(
                name="Figure out",
                depiction=StaticDepiction(
                    title="What is this place?",
                    description=(
                        "This place resembles something familiar. It takes some time to figure "
                        "it out, but you are sure it does not belong to the creator of this place."
                    ),
                    image="uncertainty.svg",
                ),
                outcome=StaticOutcome(
                    target=LocationId.HOME.value,
                    consequences=[
                        StaticConsequence(
                            depiction=StaticDepiction(
                                title="Credits",
                                description=(
                                    "You have recognized the artwork and the way to present "
                                    "a story. He must have added proper references in credits."
                                ),
                                image="light-bulb.svg",
                            ),
                            details=[
                                StaticDetail(
                                    description=(
                                        "Andrew seems to be a fan of the incredible game "
                                        "\"Sunless Sea.\" This place tries to mimic some "
                                        "of its mechanics, though not good enough."
                                    ),
                                    image="buoy.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "These icons are gorgeous. "
                                        "You remember watching them on game-icons.net."
                                    ),
                                    image="mona-lisa.svg",
                                ),
                            ],
                            resolution="Go back",
                        ),
                    ],
                ),
            ),
        ),
    )
