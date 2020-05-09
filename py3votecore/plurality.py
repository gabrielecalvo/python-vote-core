from .abstract_classes import AbstractSingleWinnerVotingSystem
from .plurality_at_large import PluralityAtLarge


class Plurality(AbstractSingleWinnerVotingSystem):
    def __init__(self, ballots, tie_breaker=None, random_seed=None):
        super().__init__(ballots, PluralityAtLarge, tie_breaker=tie_breaker, random_seed=random_seed)
