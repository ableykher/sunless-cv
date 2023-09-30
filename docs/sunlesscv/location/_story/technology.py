"""Module with the technology location of Sunless CV."""

from sunlessadventure.core.depiction.static import StaticDepiction
from sunlessadventure.core.outcome.static import StaticDetail, StaticConsequence, StaticOutcome
from sunlessadventure.core.action.static import StaticAction
from sunlessadventure.core.location.static import StaticExit

from sunlesscv.identifier import LocationId, CompetenceId
from sunlesscv.location.stable import StableLocation


def create_technology_location(location_tracker, watch_tracker, competence_tracker):
    """Get technology location.

    :param location_tracker: a tracker of the locations of Sunless CV
    :type: :class:`LocationTracker <sunlesscv.progress.location.LocationTracker>`
    :param watch_tracker: a tracker of the watched status in Sunless CV
    :type: :class:`WatchTracker <sunlesscv.progress.watch.WatchTracker>`
    :param competence_tracker: a competence tracker of Sunless CV
    :type: :class:`LocationTracker <sunlesscv.progress.competence.CompetenceTracker>`
    :returns: technology location
    :rtype: :class:`StableLocation <sunlesscv.location.stable.StableLocation>`
    """
    return StableLocation(
        location_tracker=location_tracker,
        watch_tracker=watch_tracker,
        location_id=LocationId.TECHNOLOGY.value,
        depiction=StaticDepiction(
            title="Skills",
            description=(
                "Your keen eyes spot a lot of details with ease. "
                "You might not have found everything, but you have enough data. "
                "What exactly did you wish to discover?"
            ),
            image="puzzle.svg",
        ),
        actions=[
            _TechnologyAction(
                name="Check",
                depiction=StaticDepiction(
                    title="Buzzword checklist",
                    description=(
                        "You have come prepared, have not you? "
                        "You take a folded piece of paper out of your left pocket. "
                        "Modern job descriptions look surprisingly alike, so "
                        "you researched and created this list with the wide-spread requirements. "
                        "All you need to do is to tick the appropriate boxes."
                    ),
                    image="folded-paper.svg",
                ),
                outcome=StaticOutcome(
                    target=LocationId.TECHNOLOGY.value,
                    consequences=[
                        StaticConsequence(
                            depiction=StaticDepiction(
                                title="Check, check, check. Done!",
                                description="It was quick and efficient.",
                                image="checklist.svg",
                            ),
                            resolution="Done",
                            details=[
                                StaticDetail(
                                    description=(
                                        "Agile. Scrum, Kanban, even SAFe. "
                                        "Three amigos, retrospective meetings. "
                                        "He seemed to be highly involved in the process."
                                    ),
                                    image="check-mark.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "BDD. Java \"Cucumber\" and Python \"behave\" are clearly "
                                        "in his toolset, although he tried to conceal all mentions "
                                        "of them."
                                    ),
                                    image="check-mark.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "ISTQB or TMap certification. "
                                        "You notice several books to train a certified specialist. "
                                        "Though not a single certificate."
                                    ),
                                    image="cross-mark.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "API. Tests, mocks, stubs, even implementations. "
                                        "You have found all kinds of tools, approaches, and "
                                        "protocols. REST and RPC. JSON, WS, plain XML, SOAP."
                                    ),
                                    image="check-mark.svg",
                                ),
                                StaticDetail(
                                    description="Selenium. Selenium grid + Python client wrappers.",
                                    image="check-mark.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Docker. He confidently used it in several companies, "
                                        "though he did not configure the infrastructure. "
                                        "Wait, is it k8s with Windows nodes? "
                                        "Well, it was a bit too optimistic, was not it?"
                                    ),
                                    image="check-mark.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "CI. You get quite skeptical when you see the list of "
                                        "CI servers: TeamCity, Bamboo, Jenkins, Travis CI, "
                                        "Github Actions, Circle CI. "
                                        "Has he had enough time to master at least half of them? "
                                        "Albeit, he uses Travis CI and Github Actions for "
                                        "his pet projects."
                                    ),
                                    image="check-mark.svg",
                                ),
                            ],
                        ),
                    ],
                ),
                competence_tracker=competence_tracker,
                competence_ids=[
                    CompetenceId.AGILE.value,
                    CompetenceId.BDD.value,
                    CompetenceId.CI.value,
                    CompetenceId.CONTAINER.value,
                    CompetenceId.PROTOCOL.value,
                    CompetenceId.PYTHON.value,
                    CompetenceId.SELENIUM.value,
                ],
            ),
            _TechnologyAction(
                name="Find out",
                depiction=StaticDepiction(
                    title="Quality Assurance",
                    description=(
                        "Most of his work experience is related to QA. "
                        "What did he learn?"
                    ),
                    image="ladybug.svg",
                ),
                outcome=StaticOutcome(
                    target=LocationId.TECHNOLOGY.value,
                    consequences=[
                        StaticConsequence(
                            depiction=StaticDepiction(
                                title="Quality Assurance",
                                description=(
                                    "It can take the whole day. "
                                    "Priorities of the projects make QA processes quite different "
                                    "among the companies. "
                                    "You decided to focus on the common aspects."
                                ),
                                image="ladybug.svg",
                            ),
                            resolution="Go back",
                            details=[
                                StaticDetail(
                                    description=(
                                        "Test design. One can easily spot frequently used "
                                        "techniques, such as partitioning and randomization. "
                                        "A bunch of decision trees, orthogonal tables, and "
                                        "mind maps imply that there is much more to find."
                                    ),
                                    image="pencil-brush.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Test automation. You are quickly overwhelmed "
                                        "with the information. It may be wise to focus "
                                        "your search specifically on test automation."
                                    ),
                                    image="auto-repair.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Test management. The variety of tools "
                                        "drew your attention: standalone applications "
                                        "like TestRail and TestLink, Jira plugins, such as "
                                        "Zephyr and Xray, even mind maps. "
                                        "A nasty remark about HP QC makes you stop looking further."
                                    ),
                                    image="family-tree.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "What?! Andrew has no certificates! "
                                        "Not even the ISTQB Foundation Level. "
                                        "Can you trust his knowledge? "
                                        "Well, several companies assessed him, and he succeeded. "
                                        "Perhaps, test certificates don't matter that much."
                                    ),
                                    image="diploma.svg",
                                ),
                            ],
                        ),
                    ],
                ),
                competence_tracker=competence_tracker,
                competence_ids=[
                    CompetenceId.QA.value,
                    CompetenceId.TEST_AUTOMATION.value,
                    CompetenceId.TEST_DESIGN.value,
                    CompetenceId.TMS.value,
                ],
            ),
            _TechnologyAction(
                name="Find out",
                depiction=StaticDepiction(
                    title="Test Automation",
                    description=(
                        "These green and red lights annoy you. Everybody knows what they mean. "
                        "Does he know more than the colors of successful and failed tests?"
                    ),
                    image="ladybug-cog.svg",
                ),
                outcome=StaticOutcome(
                    target=LocationId.TECHNOLOGY.value,
                    consequences=[
                        StaticConsequence(
                            depiction=StaticDepiction(
                                title="Test Automation",
                                description=(
                                    "One of the computers was left unlocked. "
                                    "You opened the terminal and started typing commands. "
                                    "After a couple of hours, you know what is going on "
                                    "in the room. Moreover, you know how it operates."
                                ),
                                image="ladybug-cog.svg",
                            ),
                            resolution="Go back",
                            details=[
                                StaticDetail(
                                    description=(
                                        "Programming languages. "
                                        "Python is almost everywhere. "
                                        "Here and there, Java takes over if it suits better. "
                                        "There are also old code snippets written in C++ and Perl. "
                                        "It seems to be it, though you suspect "
                                        "there should be Typescript somewhere."
                                    ),
                                    image="lockpicks.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Test frameworks. It appears that he finds pytest "
                                        "powerful yet intricate. Other packages such as "
                                        "Python unittest, Java Junit, and JS Mocha are "
                                        "also a known territory for him. There are traces "
                                        "of multiple BDD frameworks: Python behave, "
                                        "Java Cucumber, though he tends to avoid them."
                                    ),
                                    image="swiss-army-knife.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "CI servers. A couple of TeamCity templates "
                                        "produce a dozen configurations, creating "
                                        "an attentive structure of isolated test scenarios. "
                                        "Some employers relied on the Atlassian suite with Bamboo. "
                                        "There are also a few Jenkins scripts, "
                                        "though the quality is questionable. "
                                        "It is good to see that his pet projects depend on "
                                        "Travis CI and Github Actions."
                                    ),
                                    image="factory-arm.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Reports. Allure plugin for pytest, allure plugins "
                                        "for TeamCity and Bamboo. "
                                        "He loves these human-readable reports. "
                                        "What about machines? "
                                        "Junit format seems to fit all other purposes."
                                    ),
                                    image="histogram.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Environment management. You appreciate the variety "
                                        "of platforms. Both Windows and a few Linux distributives "
                                        "(namely RHEL, CentOS, Mint, Ubuntu) are present. "
                                        "Andrew automated creation and management of Docker "
                                        "containers and virtual machines (VMWare, Hyper-V), "
                                        "though you found no records of infrastructure "
                                        "administration. It might be a good thing as the teams "
                                        "delegated the responsibility to experts."
                                    ),
                                    image="server-rack.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Load testing. One can't call Andrew an expert "
                                        "in load testing. However, a couple of solutions "
                                        "drew your attention. Namely, he used Yandex.Tank "
                                        "to integrate load tests into the CI process "
                                        "via TeamCity builds. Besides, he used Locust "
                                        "when the RPS-based approach was not feasible."
                                    ),
                                    image="weight.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Code coverage. It is assuring to see that he measures "
                                        "the code coverage in his pet projects with the pytest-cov "
                                        "plugin. Even though the metric is 100%, "
                                        "he seemed to be quite skeptical about it at work."
                                    ),
                                    image="high-tide.svg",
                                ),
                            ],
                        ),
                    ],
                ),
                competence_tracker=competence_tracker,
                competence_ids=[
                    CompetenceId.CI.value,
                    CompetenceId.CONTAINER.value,
                    CompetenceId.JAVA.value,
                    CompetenceId.LOAD_TESTING.value,
                    CompetenceId.PYTHON.value,
                    CompetenceId.REPORT.value,
                    CompetenceId.TEST_AUTOMATION.value,
                    CompetenceId.VIRTUAL_MACHINE.value,
                ],
            ),
        ],
        exit_=StaticExit(name="That's enough", target=LocationId.PROFESSION.value),
    )


class _TechnologyAction(StaticAction):
    """Class to manage an action for a technology."""

    def __init__(self, name, depiction, outcome, competence_tracker, competence_ids=()):
        # pylint: disable=too-many-arguments
        super().__init__(name=name, depiction=depiction, outcome=outcome)
        self.__competence_tracker = competence_tracker
        self.__competence_ids = tuple(competence_ids)

    def perform(self):
        """Perform an action.

        :returns: outcome of the action
        :rtype: :class:`Outcome <sunlessadventure.abstract.outcome.Outcome>`
        """
        outcome = super().perform()
        for competence_id in self.__competence_ids:
            self._competence_tracker.discover(competence_id=competence_id)
        return outcome

    @property
    def _competence_tracker(self):
        """Competence tracker."""
        return self.__competence_tracker
