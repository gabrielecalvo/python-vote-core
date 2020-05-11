from .common_functions import get_candidates_from_ballots
import random


class RandomWinner:
    def __init__(self, ballots, random_seed=None):
        self.candidates = get_candidates_from_ballots(ballots)
        self.random = random.Random(random_seed)

    def as_dict(self):
        placements = sorted(self.candidates)
        self.random.shuffle(placements)
        return {
            "candidates": self.candidates,
            "winner": placements[0],
            "placements": [{'candidates': [i]} for i in placements]
        }