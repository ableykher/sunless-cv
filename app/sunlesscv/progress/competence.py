"""Module with a tracker for the competences of Sunless CV."""

from sunlesscv.identifier import CompetenceId
from sunlesscv.progress.abstract import AbstractTracker


class CompetenceTracker(AbstractTracker):
    """Class to track discovered competences."""

    def __init__(self, valid_competence_ids=None):
        super().__init__()
        self._discovered_competence_ids = set()

        if valid_competence_ids is None:
            valid_competence_ids = set(competence_id.value for competence_id in CompetenceId)
        self._valid_competence_ids = frozenset(
            str(competence_id) for competence_id in valid_competence_ids
        )

    def discover(self, competence_id):
        """Mark a competence as discovered.

        :param competence_id: identifier of the competence
        :type: str
        """
        competence_id = str(competence_id)
        if competence_id in self._valid_competence_ids:
            self._discovered_competence_ids.add(competence_id)

    def get_progress_percentage(self):
        """Get current progress.

        :returns: progress percentage
        :rtype: float
        """
        total = len(self._valid_competence_ids)

        if total == 0:
            return 0

        return 100 * len(self._discovered_competence_ids) / total
