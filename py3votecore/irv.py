from .abstract_classes import AbstractSingleWinnerVotingSystem
from .stv import STV
from .common_functions import get_placement_from_tallies


class IRV(AbstractSingleWinnerVotingSystem):
    def __init__(self, ballots, tie_breaker=None, random_seed=None):
        super().__init__(ballots, STV, tie_breaker=tie_breaker, random_seed=random_seed)

    def calculate_results(self):
        super().calculate_results()
        IRV.singularize(self.rounds)

    def as_dict(self):
        data = super().as_dict()
        IRV.singularize(data["rounds"])
        data['placements'] = get_placement_from_tallies(data["rounds"][-1]["tallies"])
        return data

    @staticmethod
    def singularize(rounds):
        for r in rounds:
            if "winners" in r:
                r["winner"] = list(r["winners"])[0]
                del r["winners"]
