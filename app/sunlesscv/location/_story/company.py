"""Module with the company location of Sunless CV."""

from sunlessadventure.core.depiction.static import StaticDepiction
from sunlessadventure.core.outcome.static import StaticDetail, StaticConsequence, StaticOutcome
from sunlessadventure.core.action.static import StaticAction
from sunlessadventure.core.location.static import StaticExit

from sunlesscv.identifier import LocationId, CompetenceId
from sunlesscv.location.stable import StableLocation


def create_company_location(location_tracker, watch_tracker, competence_tracker):
    """Get company location.

    :param location_tracker: a tracker of the locations of Sunless CV
    :type: :class:`LocationTracker <sunlesscv.progress.location.LocationTracker>`
    :param watch_tracker: a tracker of the watched status in Sunless CV
    :type: :class:`WatchTracker <sunlesscv.progress.watch.WatchTracker>`
    :param competence_tracker: a competence tracker of Sunless CV
    :type: :class:`LocationTracker <sunlesscv.progress.competence.CompetenceTracker>`
    :returns: company location
    :rtype: :class:`StableLocation <sunlesscv.location.stable.StableLocation>`
    """
    return StableLocation(
        location_tracker=location_tracker,
        watch_tracker=watch_tracker,
        location_id=LocationId.COMPANY.value,
        depiction=StaticDepiction(
            title="Companies",
            description=(
                "It took time, but you deciphered everything and "
                "made a deck of cards with short summaries."
            ),
            image="stack.svg",
        ),
        actions=[
            _CompanyAction(
                depiction=StaticDepiction(
                    title="Ohpen",
                    description="September 2019 - February 2020. QA automation engineer.",
                    image="card-draw.svg",
                ),
                outcome=StaticOutcome(
                    target=LocationId.COMPANY.value,
                    consequences=[
                        StaticConsequence(
                            depiction=StaticDepiction(
                                title="Ohpen, Amsterdam, Netherlands",
                                description=(
                                    "September 2019 - February 2020. "
                                    "QA automation engineer."
                                ),
                                image="look-at.svg",
                            ),
                            resolution="Go back",
                            details=[
                                StaticDetail(
                                    description=(
                                        "Created a PoC for a service to collect "
                                        "the status of the product API so that actual, "
                                        "deprecated, and no longer used endpoints are "
                                        "clearly separated and tested accordingly."
                                    ),
                                    image="medical-thermometer.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Created a PoC for a test automation framework. "
                                        "Existing frameworks did not satisfy the needs, "
                                        "so a new framework had to be introduced."
                                    ),
                                    image="vintage-robot.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Supported existing frameworks "
                                        "(mostly code review)."
                                    ),
                                    image="fire-extinguisher.svg",
                                ),
                            ],
                        ),
                    ],
                ),
                competence_tracker=competence_tracker,
                competence_ids=[
                    CompetenceId.API.value,
                    CompetenceId.TEST_AUTOMATION.value,
                    CompetenceId.WEB_APPLICATION.value,
                ],
            ),
            _CompanyAction(
                depiction=StaticDepiction(
                    title="Fedex / TNT Digital International",
                    description="May 2019 - August 2019. QA tester.",
                    image="card-draw.svg",
                ),
                outcome=StaticOutcome(
                    target=LocationId.COMPANY.value,
                    consequences=[
                        StaticConsequence(
                            depiction=StaticDepiction(
                                title=(
                                    "Fedex / TNT Digital International, "
                                    "Hoofddorp, Netherlands"
                                ),
                                description="May 2019 - August 2019. QA tester.",
                                image="look-at.svg",
                            ),
                            resolution="Go back",
                            details=[
                                StaticDetail(
                                    description=(
                                        "Played the role of a QA engineer in a scrum team. "
                                        "Mostly manual testing."
                                    ),
                                    image="cherish.svg",
                                ),
                            ],
                        ),
                    ],
                ),
                competence_tracker=competence_tracker,
                competence_ids=[
                    CompetenceId.AGILE.value,
                    CompetenceId.QA.value,
                ],
            ),
            _CompanyAction(
                depiction=StaticDepiction(
                    title="Nice Ltd.",
                    description="March 2018 - March 2019. Senior QA Engineer.",
                    image="card-draw.svg",
                ),
                outcome=StaticOutcome(
                    target=LocationId.COMPANY.value,
                    consequences=[
                        StaticConsequence(
                            depiction=StaticDepiction(
                                title="Nice Ltd., Alkmaar, Netherlands",
                                description="March 2018 - March 2019. Senior QA Engineer.",
                                image="look-at.svg",
                            ),
                            resolution="Go back",
                            details=[
                                StaticDetail(
                                    description=(
                                        "Performed product risk assessment to provide "
                                        "a testing strategy for new features."
                                    ),
                                    image="slalom.svg",
                                ),
                                StaticDetail(
                                    description="Designed and executed test cases.",
                                    image="checklist.svg",
                                ),
                                StaticDetail(
                                    description="Set up testing and demo environments.",
                                    image="crane.svg",
                                ),
                                StaticDetail(
                                    description="Created and maintained CI builds.",
                                    image="factory-arm.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Improved product documentation. The team started "
                                        "to document new requirements and "
                                        "technical solutions as well as "
                                        "to restore missing documentation."
                                    ),
                                    image="spell-book.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Introduced a way to assess performance in cases "
                                        "where a standard RPS approach was not feasible."
                                    ),
                                    image="cricket.svg",
                                ),
                            ],
                        ),
                    ],
                ),
                competence_tracker=competence_tracker,
                competence_ids=[
                    CompetenceId.CI.value,
                    CompetenceId.LOAD_TESTING.value,
                    CompetenceId.RISK_ASSESSMENT.value,
                    CompetenceId.STANDALONE_APPLICATION.value,
                    CompetenceId.TEST_DESIGN.value,
                    CompetenceId.VIRTUAL_MACHINE.value,
                ],
            ),
            _CompanyAction(
                depiction=StaticDepiction(
                    title="Tinkoff bank",
                    description="December 2016 - January 2018. Lead specialist.",
                    image="card-draw.svg",
                ),
                outcome=StaticOutcome(
                    target=LocationId.COMPANY.value,
                    consequences=[
                        StaticConsequence(
                            depiction=StaticDepiction(
                                title="Tinkoff bank, Moscow, Russia",
                                description=(
                                    "December 2016 - January 2018. Lead specialist."
                                ),
                                image="look-at.svg",
                            ),
                            resolution="Go back",
                            details=[
                                StaticDetail(
                                    description=(
                                        "Set up the test automation for multiple projects. "
                                        "The process includes test design, code review, "
                                        "framework setup and maintenance, "
                                        "CI configuration, etc..."
                                    ),
                                    image="auto-repair.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Implemented integration between test execution "
                                        "and the test management tool. As a result, "
                                        "everyone can request the test automation and "
                                        "review its outcome in one place during runtime."
                                    ),
                                    image="cycle.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Created a build plan to perform load tests "
                                        "on demand. Any team member can provide "
                                        "a host address and a load profile to launch "
                                        "a new performance test."
                                    ),
                                    image="tank.svg",
                                ),
                            ],
                        ),
                    ],
                ),
                competence_tracker=competence_tracker,
                competence_ids=[
                    CompetenceId.CI.value,
                    CompetenceId.LOAD_TESTING.value,
                    CompetenceId.QA.value,
                    CompetenceId.REPORT.value,
                    CompetenceId.TEST_AUTOMATION.value,
                    CompetenceId.TEST_DESIGN.value,
                    CompetenceId.TMS.value,
                ],
            ),
            _CompanyAction(
                depiction=StaticDepiction(
                    title="Align Technology Inc.",
                    description="June 2016 - December 2016. Senior SQA Engineer.",
                    image="card-draw.svg",
                ),
                outcome=StaticOutcome(
                    target=LocationId.COMPANY.value,
                    consequences=[
                        StaticConsequence(
                            depiction=StaticDepiction(
                                title="Align Technology Inc., Moscow, Russia",
                                description=(
                                    "June 2016 - December 2016. Senior SQA Engineer."
                                ),
                                image="look-at.svg",
                            ),
                            resolution="Go back",
                            details=[
                                StaticDetail(
                                    description="Designed and executed manual test cases.",
                                    image="cherish.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Implemented feature-files and steps "
                                        "for the BDD framework."
                                    ),
                                    image="brick-pile.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Supported CI configurations. In collaboration "
                                        "with the tooling team moved the test execution "
                                        "to containers, as the shared environment "
                                        "caused issues."
                                    ),
                                    image="cargo-ship.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Provided weekly reports with the progress "
                                        "of the team."
                                    ),
                                    image="histogram.svg",
                                ),
                            ],
                        ),
                    ],
                ),
                competence_tracker=competence_tracker,
                competence_ids=[
                    CompetenceId.BDD.value,
                    CompetenceId.CI.value,
                    CompetenceId.CONTAINER.value,
                    CompetenceId.QA.value,
                    CompetenceId.REPORT.value,
                    CompetenceId.TEST_AUTOMATION.value,
                    CompetenceId.TEST_DESIGN.value,
                ],
            ),
            _CompanyAction(
                depiction=StaticDepiction(
                    title="Infowatch",
                    description=(
                        "November 2013 - March 2016. Senior QA Automation Engineer."
                    ),
                    image="card-draw.svg",
                ),
                outcome=StaticOutcome(
                    target=LocationId.COMPANY.value,
                    consequences=[
                        StaticConsequence(
                            depiction=StaticDepiction(
                                title="Infowatch, Moscow, Russia",
                                description=(
                                    "November 2013 - March 2016. "
                                    "Senior QA Automation Engineer."
                                ),
                                image="look-at.svg",
                            ),
                            resolution="Go back",
                            details=[
                                StaticDetail(
                                    description=(
                                        "Played the role of a technical lead in the team "
                                        "of QA automation engineers."
                                    ),
                                    image="teacher.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Designed and implemented autotests based on "
                                        "checklists and test cases for manual execution. "
                                        "Thus the requirements coverage was measured and "
                                        "synchronized between auto- and manual tests."
                                    ),
                                    image="shaking-hands.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Regularly researched existing packages or created "
                                        "new libraries to simulate user activities, "
                                        "such as instant messaging, email sending, "
                                        "printing, etc."
                                    ),
                                    image="erlenmeyer.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Managed the test automation infrastructure."
                                    ),
                                    image="server-rack.svg",
                                ),
                                StaticDetail(
                                    description="Performed regular code reviews.",
                                    image="cyber-eye.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Implemented a system to create a fully functional "
                                        "testing environment automatically. "
                                        "Such environments consist of several virtual "
                                        "machines and client-server applications. "
                                        "Successful execution leads to an automatic "
                                        "cleanup, including the removal of the VMs."
                                    ),
                                    image="factory-arm.svg",
                                ),
                                StaticDetail(
                                    description=(
                                        "Introduced an efficient process to locate and "
                                        "fix product issues found by test automation. "
                                        "When an error occurred, the corresponding "
                                        "environment was suspended and used later for the "
                                        "investigation by a QA engineer or a developer. "
                                        "Therefore, test automation saved "
                                        "the host resources while everyone could still "
                                        "reproduce the issue."
                                    ),
                                    image="auto-repair.svg",
                                ),
                            ],
                        ),
                    ],
                ),
                competence_tracker=competence_tracker,
                competence_ids=[
                    CompetenceId.CI.value,
                    CompetenceId.PROTOCOL.value,
                    CompetenceId.QA.value,
                    CompetenceId.REPORT.value,
                    CompetenceId.STANDALONE_APPLICATION.value,
                    CompetenceId.TEST_AUTOMATION.value,
                    CompetenceId.TEST_DESIGN.value,
                    CompetenceId.VIRTUAL_MACHINE.value,
                ],
            ),
            _CompanyAction(
                depiction=StaticDepiction(
                    title="Acronis",
                    description="September 2012 - November 2013. Associate QA Tester.",
                    image="card-draw.svg",
                ),
                outcome=StaticOutcome(
                    target=LocationId.COMPANY.value,
                    consequences=[
                        StaticConsequence(
                            depiction=StaticDepiction(
                                title="Acronis, Moscow, Russia",
                                description=(
                                    "September 2012 - November 2013. Associate QA Tester."
                                ),
                                image="look-at.svg",
                            ),
                            resolution="Go back",
                            details=[
                                StaticDetail(
                                    description=(
                                        "Implemented test cases created by manual "
                                        "QA engineers."
                                    ),
                                    image="shaking-hands.svg",
                                ),
                                StaticDetail(
                                    description="Maintained test automation framework.",
                                    image="spanner.svg",
                                ),
                                StaticDetail(
                                    description="Maintained virtual machine templates.",
                                    image="mechanic-garage.svg",
                                ),
                            ],
                        ),
                    ],
                ),
                competence_tracker=competence_tracker,
                competence_ids=[
                    CompetenceId.QA.value,
                    CompetenceId.STANDALONE_APPLICATION.value,
                    CompetenceId.TEST_AUTOMATION.value,
                    CompetenceId.VIRTUAL_MACHINE.value,
                ],
            ),
            _CompanyAction(
                depiction=StaticDepiction(
                    title="Yandex",
                    description="February 2012 - September 2012. Intern Developer.",
                    image="card-draw.svg",
                ),
                outcome=StaticOutcome(
                    target=LocationId.COMPANY.value,
                    consequences=[
                        StaticConsequence(
                            depiction=StaticDepiction(
                                title="Yandex, Moscow, Russia",
                                description=(
                                    "February 2012 - September 2012. Intern Developer."
                                ),
                                image="look-at.svg",
                            ),
                            resolution="Go back",
                            details=[
                                StaticDetail(
                                    description=(
                                        "Researched and implemented algorithms to assess "
                                        "and predict the rate of click on ad banners."
                                    ),
                                    image="erlenmeyer.svg",
                                ),
                            ],
                        ),
                    ],
                ),
                competence_tracker=competence_tracker,
                competence_ids=[
                    CompetenceId.WEB_APPLICATION.value,
                ],
            ),
        ],
        exit_=StaticExit(name="Enough reading", target=LocationId.PROFESSION.value),
    )


class _CompanyAction(StaticAction):
    """Class to manage an action for a company."""

    def __init__(self, depiction, outcome, competence_tracker, competence_ids=()):
        super().__init__(name="Flip", depiction=depiction, outcome=outcome)
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
