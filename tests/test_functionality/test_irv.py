# Copyright (C) 2009, Brad Beattie
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from py3votecore.irv import IRV
import unittest


class TestInstantRunoff(unittest.TestCase):

    # IRV, no ties
    def test_irv_no_ties(self):

        # Generate data
        input = [
            {"count": 26, "ballot": ["c1", "c2", "c3"]},
            {"count": 20, "ballot": ["c2", "c3", "c1"]},
            {"count": 23, "ballot": ["c3", "c1", "c2"]},
        ]
        output = IRV(input, random_seed=0).as_dict()

        # Run tests
        self.assertEqual(
            output,
            {
                "candidates": {"c1", "c2", "c3"},
                "quota": 35,
                "winner": "c3",
                "rounds": [
                    {"tallies": {"c3": 23.0, "c2": 20.0, "c1": 26.0}, "loser": "c2"},
                    {"tallies": {"c3": 43.0, "c1": 26.0}, "winner": "c3"},
                ],
                'placements': [{'candidates': {'c3'}, 'points': 43.0},
                               {'candidates': {'c1'}, 'points': 26.0}],
            },
        )

    # IRV, ties
    def test_irv_ties(self):

        # Generate data
        input = [
            {"count": 26, "ballot": ["c1", "c2", "c3"]},
            {"count": 20, "ballot": ["c2", "c3", "c1"]},
            {"count": 20, "ballot": ["c3", "c1", "c2"]},
        ]
        output = IRV(input, random_seed=0).as_dict()

        # Run tests
        self.assertEqual(
            output,
            {
                "candidates": {"c3", "c2", "c1"},
                "quota": 34,
                "rounds": [
                    {
                        "loser": "c2",
                        "tallies": {"c1": 26.0, "c2": 20.0, "c3": 20.0},
                        "tied_losers": {"c3", "c2"},
                    },
                    {"tallies": {"c1": 26.0, "c3": 40.0}, "winner": "c3"},
                ],
                "tie_breaker": ["c1", "c3", "c2"],
                "winner": "c3",
                'placements': [{'candidates': {'c3'}, 'points': 40.0},
                               {'candidates': {'c1'}, 'points': 26.0}],
            },
        )

    # IRV, no rounds
    def test_irv_landslide(self):

        # Generate data
        input = [
            {"count": 56, "ballot": ["c1", "c2", "c3"]},
            {"count": 20, "ballot": ["c2", "c3", "c1"]},
            {"count": 20, "ballot": ["c3", "c1", "c2"]},
        ]
        output = IRV(input, random_seed=0).as_dict()

        # Run tests
        self.assertEqual(
            output,
            {
                "candidates": {"c1", "c2", "c3"},
                "quota": 49,
                "winner": "c1",
                "rounds": [
                    {"tallies": {"c3": 20.0, "c2": 20.0, "c1": 56.0}, "winner": "c1"}
                ],
                'placements': [{'candidates': {'c1'}, 'points': 56.0},
                               {'candidates': {'c2', 'c3'}, 'points': 20.0}],
            },
        )


if __name__ == "__main__":
    unittest.main()
