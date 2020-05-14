from .common_functions import ensure_listlike, get_placement_from_tallies, get_candidates_from_ballots
from collections import defaultdict
from .tie_breaker import TieBreaker
from copy import deepcopy


class BordaCount:
    def __init__(self, ballots, tie_breaker=None, random_seed=None, weights=None):
        self.ballots = ballots
        self.tie_breaker = tie_breaker
        self.random_seed = random_seed
        self.weights = weights

        self.candidates = None
        self.tallies = None
        self.placement = None
        self.winner = None
        self.validate()

    def validate(self):
        ballot_lengths = [len(ensure_listlike(b["ballot"])) for b in self.ballots]
        max_ballot_length = max(ballot_lengths)

        self.candidates = get_candidates_from_ballots(self.ballots)
        assert len(self.candidates) >= max_ballot_length, "Ballot cannot be longer than number of candidates!"

        self.weights = self.weights or list(range(max_ballot_length, 0, -1))
        assert len(self.weights) == max_ballot_length, "Weights must be the same length as the longest ballot!"

    def calculate_results(self):
        self.tallies = defaultdict(float)
        for ballot in self.ballots:
            multiplier = ballot.get('count', 1)
            for candidate, weight in zip(ballot['ballot'], self.weights):
                self.tallies[candidate] += multiplier * weight
        self.tallies = dict(self.tallies)

        self.placement = get_placement_from_tallies(self.tallies)
        flatten_placement = [c for same_rank in self.placement for c in self.break_ties(same_rank['candidates'])]
        self.winner = flatten_placement[0]

    def break_ties(self, contender_list):
        ordering = TieBreaker(set(contender_list), random_seed=self.random_seed).random_ordering
        return ordering

    def as_dict(self):
        self.calculate_results()
        data = {
            "candidates": self.candidates,
            "rounds": [
                {
                    "winner": self.winner,
                    "tallies": self.tallies,
                }
            ],
            "winner": self.winner,
            "placements": get_placement_from_tallies(self.tallies)
        }
        return data
