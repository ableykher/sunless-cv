"""Module with the profession location of Sunless CV."""

from sunlessadventure.core.depiction.static import StaticDepiction
from sunlessadventure.core.outcome.static import StaticOutcome
from sunlessadventure.core.action.static import StaticAction
from sunlessadventure.core.location.static import StaticExit

from sunlesscv.identifier import LocationId
from sunlesscv.location.stable import StableLocation


def create_profession_location(location_tracker, watch_tracker):
    """Get profession location.

    :param location_tracker: a tracker of the locations of Sunless CV
    :type: :class:`LocationTracker <sunlesscv.progress.location.LocationTracker>`
    :param watch_tracker: a tracker of the watched status in Sunless CV
    :type: :class:`WatchTracker <sunlesscv.progress.watch.WatchTracker>`
    :returns: profession location
    :rtype: :class:`StableLocation <sunlesscv.location.stable.StableLocation>`
    """
    return StableLocation(
        location_tracker=location_tracker,
        watch_tracker=watch_tracker,
        location_id=LocationId.PROFESSION.value,
        depiction=StaticDepiction(
            title="Profession",
            description=(
                "There is nobody in the room except you, but you sense some activity. "
                "Now and then, a few LED lights flash green or red, "
                "while several screens display a rapidly growing list of messages. "
                "You decide to pay attention only to things that make sense to you."
            ),
            image="gears.svg",
        ),
        actions=(
            StaticAction(
                name="Collect",
                depiction=StaticDepiction(
                    title="Skills",
                    description=(
                        "Familiar terms are spread all over the room. "
                        "You see them on book covers, in code snippets and diagrams. "
                        "If you can collect them, you would get a good overview of "
                        "Andrew's technical background."
                    ),
                    image="jigsaw-piece.svg",
                ),
                outcome=StaticOutcome(target=LocationId.TECHNOLOGY.value),
            ),
            StaticAction(
                name="Read",
                depiction=StaticDepiction(
                    title="Companies",
                    description=(
                        "There are dozens of branded notebooks covered with handwriting, figures, "
                        "and schemes. Perhaps they can shed some light on "
                        "Andrew's responsibilities within these companies."
                    ),
                    image="archive-research.svg",
                ),
                outcome=StaticOutcome(target=LocationId.COMPANY.value),
            ),
        ),
        exit_=StaticExit(name="Leave", target=LocationId.HALLWAY.value),
    )
