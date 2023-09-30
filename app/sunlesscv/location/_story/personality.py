"""Module with the personality location of Sunless CV."""

from sunlessadventure.core.depiction.static import StaticDepiction
from sunlessadventure.core.outcome.static import StaticDetail, StaticConsequence, StaticOutcome
from sunlessadventure.core.action.static import StaticAction
from sunlessadventure.core.location.static import StaticExit

from sunlesscv.identifier import LocationId
from sunlesscv.location.base import Location


def create_personality_location(location_tracker, watch_tracker, distrust_tracker):
    """Get personality location.

    :param location_tracker: a tracker of the locations of Sunless CV
    :type: :class:`LocationTracker <sunlesscv.progress.location.LocationTracker>`
    :param watch_tracker: a tracker of the watched status in Sunless CV
    :type: :class:`WatchTracker <sunlesscv.progress.watch.WatchTracker>`
    :param distrust_tracker: a tracker of the distrust status in Sunless CV
    :type: :class:`DistrustTracker <sunlesscv.progress.distrust.DistrustTracker>`
    :returns: personality location
    :rtype: :class:`_PersonalityLocation`
    """
    return _PersonalityLocation(
        location_tracker=location_tracker,
        watch_tracker=watch_tracker,
        distrust_tracker=distrust_tracker,
    )


class _PersonalityLocation(Location):
    """Class to manage the personality location of Sunless CV."""

    def __init__(self, location_tracker, watch_tracker, distrust_tracker):
        super().__init__(
            location_tracker=location_tracker,
            watch_tracker=watch_tracker,
            is_watched=True,
        )
        self.__distrust_tracker = distrust_tracker

    def get_id(self):
        """Get identifier of the location.

        :returns: identifier of the location
        :rtype: str
        """
        return LocationId.PERSONALITY.value

    def get_depiction(self):
        """Get depiction of the location.

        :returns: depiction of the location
        :rtype: :class:`Depiction <sunlessadventure.abstract.depiction.Depiction>`
        """
        if self._distrust_tracker.is_distrusted:
            return StaticDepiction(
                title="Introversion",
                description=(
                    "Someone cleared the room. Only a few things left, "
                    "but they are of no interest to you. Wait, where is that little door!?"
                ),
                image="charm.svg",
            )

        return StaticDepiction(
            title="Personality",
            description=(
                "The room is not as big as you expect it to be. Perhaps, it looks smaller "
                "due to a slew of things, hardly organized."
            ),
            image="charm.svg",
        )

    def get_actions(self):
        """Get actions available in the location.

        :returns: list of available actions
        :rtype: list with instances of :class:`Action <sunlessadventure.abstract.action.Action>`
        """
        if self._distrust_tracker.is_distrusted:
            return [
                _ExitAction(
                    name="Exit",
                    depiction=StaticDepiction(
                        title="Exit",
                        description="There is nothing to do here anymore.",
                        image="walk.svg",
                    ),
                    outcome=StaticOutcome(target=LocationId.HALLWAY.value),
                    watch_tracker=self._watch_tracker,
                ),
            ]

        actions = [
            StaticAction(
                name="Read",
                depiction=StaticDepiction(
                    title="READ ME",
                    description=(
                        "Someone left a note on the table. Large letters of 'READ ME' "
                        "draw your attention. You start losing your temper. Why can't "
                        "he show himself and have a simple conversation?"
                    ),
                    image="folded-paper.svg",
                ),
                outcome=StaticOutcome(
                    target=LocationId.PERSONALITY.value,
                    consequences=[
                        StaticConsequence(
                            depiction=StaticDepiction(
                                title="Handwritten note",
                                description=(
                                    "The note is short: 'I sincerely apologize for "
                                    "not being here with you. It is hard for me to meet "
                                    "new people. Albeit, I understand how important it is "
                                    "to help other people to know me better. I mean "
                                    "no insult by avoiding you, perhaps we could be "
                                    "friends one day. Meanwhile, I kindly ask you to mind "
                                    "my personal space.'"
                                ),
                                image="folded-paper.svg",
                            ),
                            resolution="Ok",
                            details=[
                                StaticDetail(
                                    description=(
                                        "What does he mean by 'not being here'? "
                                        "Who is watching you then?"
                                    ),
                                    image="hidden.svg",
                                ),
                            ],
                        ),
                    ],
                ),
            ),
            StaticAction(
                name="Search",
                depiction=StaticDepiction(
                    title="Education",
                    description=(
                        "There are a few hints for a university. A branded hoody on "
                        "the chair's back and a diamond-shaped badge on the table depict "
                        "the same emblem. Could you find a diploma somewhere?"
                    ),
                    image="graduate-cap.svg",
                ),
                outcome=StaticOutcome(
                    target=LocationId.PERSONALITY.value,
                    consequences=[
                        StaticConsequence(
                            depiction=StaticDepiction(
                                title="Lomonosov Moscow State University",
                                description=(
                                    "Here it is. According to the diploma, Andrew studied "
                                    "mathematics from 2006 till 2011 to get "
                                    "a specialist degree. One year more than "
                                    "the bachelor's degree requires, yet one year short "
                                    "for the master's degree. You have mixed feelings "
                                    "about this. On the positive side, the diploma "
                                    "contains only excellent marks, and Andrew was "
                                    "a PhD student, though he did not graduate."
                                ),
                                image="graduate-cap.svg",
                            ),
                            resolution="Ok",
                        ),
                    ],
                ),
            ),
            StaticAction(
                name="Look around",
                depiction=StaticDepiction(
                    title="Hobbies",
                    description=(
                        "Even unorganized, the belongings tell you much about "
                        "how Andrew spends his spare time."
                    ),
                    image="body-balance.svg",
                ),
                outcome=StaticOutcome(
                    target=LocationId.PERSONALITY.value,
                    consequences=[
                        StaticConsequence(
                            depiction=StaticDepiction(
                                title="Hobbies",
                                description=(
                                    "One quick tour around the room is enough "
                                    "for the assessment."
                                ),
                                image="body-balance.svg",
                            ),
                            resolution="Ok",
                            details=[
                                StaticDetail(
                                    description=(
                                        "A red velveteen bag drew your attention. "
                                        "You opened it to find the Staunton chess set. "
                                        "After a quick search, you discover his chess.com "
                                        "account with a rating around 2000."
                                    ),
                                    image="pawn.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "One squared notebook lies open on the table. "
                                        "A stack of others resides on the shelf. "
                                        "Hand-drawn graphs and pictures, formulae, and "
                                        "a lot of binomial coefficients cover their pages. "
                                        "Based on some problem descriptions, one can "
                                        "assume these are from math olympiads."
                                    ),
                                    image="diagram.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "A noticeable pyramid on a cupboard turns out "
                                        "to be a dozen board games. Most titles "
                                        "on cardboard boxes are in Russian, but you don't "
                                        "need to see a name to recognize some of them."
                                    ),
                                    image="rolling-dices.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Looking into Andrew's browser history, you came "
                                        "across a video from his childhood. The young boy "
                                        "plays the piano, making faces and fooling around "
                                        "at the same time. It must be awkward for him "
                                        "to watch this video. He could not become "
                                        "a skillful pianist with such attitude, though "
                                        "he developed an urge to play from time to time. "
                                        "A digital piano in the room helps him with that."
                                    ),
                                    image="piano-keys.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Two sets of uniforms have his surname on it: "
                                        "dark blue and green with black. The latter is "
                                        "the corporate colors of InfoWatch. You checked "
                                        "the pictures on social media. His colleagues "
                                        "became game partners and friends, as he kept playing "
                                        "with them long after he left the company."
                                    ),
                                    image="volleyball-ball.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "It is obvious Andrew loves \"Sunless Sea.\" "
                                        "His steam account reveals another "
                                        "half a hundred games."
                                    ),
                                    image="gamepad.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "A badge on the backpack gives you a subtle smile. "
                                        "It resembles a tiny blood pack with a plastic "
                                        "needle. Now you know his blood type and "
                                        "feel awkward and funny at the same time."
                                    ),
                                    image="heart-drop.svg",
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        ]

        if self._location_tracker.get_progress_percentage() > 60:
            actions.append(
                _SecretAction(
                    name="Push",
                    depiction=StaticDepiction(
                        title="Hidden door",
                        description=(
                            "A little door almost left unnoticed. Was it even here before? "
                            "Someone intentionally concealed it. Anything behind this door "
                            "must tell you more than everything in the room, right?"
                        ),
                        image="secret-door.svg",
                    ),
                    outcome=StaticOutcome(
                        target=LocationId.HALLWAY.value,
                        consequences=[
                            StaticConsequence(
                                depiction=StaticDepiction(
                                    title="Wrong!",
                                    description=(
                                        "You remember approaching the door but nothing else. "
                                        "Someone made you lose consciousness and dragged "
                                        "you out. On the bright side, nobody is watching you."
                                    ),
                                    image="knockout.svg",
                                ),
                                resolution="Ok",
                            ),
                        ],
                    ),
                    watch_tracker=self._watch_tracker,
                    distrust_tracker=self._distrust_tracker,
                ),
            )

        return actions

    def get_exit(self):
        """Get exit.

        :returns: information about the exit from the location
        :rtype: :class:`StaticExit <sunlessadventure.core.location.static.StaticExit>`
        """
        return StaticExit(name="Leave", target=LocationId.HALLWAY.value)

    @property
    def _distrust_tracker(self):
        """Distrust tracker."""
        return self.__distrust_tracker


class _ExitAction(StaticAction):
    """Class to manage an action that leaves the location."""

    def __init__(self, name, depiction, outcome, watch_tracker):
        super().__init__(name=name, depiction=depiction, outcome=outcome)
        self.__watch_tracker = watch_tracker

    def perform(self):
        """Perform an action.

        :returns: outcome of the action
        :rtype: :class:`Outcome <sunlessadventure.abstract.outcome.Outcome>`
        """
        outcome = super().perform()
        self.__watch_tracker.is_watched = False
        return outcome


class _SecretAction(_ExitAction):
    """Class to manage the secret action."""

    def __init__(self, name, depiction, outcome, watch_tracker, distrust_tracker):
        # pylint: disable=too-many-arguments
        super().__init__(
            name=name,
            depiction=depiction,
            outcome=outcome,
            watch_tracker=watch_tracker,
        )
        self.__distrust_tracker = distrust_tracker

    def perform(self):
        """Perform an action.

        :returns: outcome of the action
        :rtype: :class:`Outcome <sunlessadventure.abstract.outcome.Outcome>`
        """
        outcome = super().perform()
        self.__distrust_tracker.is_distrusted = True
        return outcome
