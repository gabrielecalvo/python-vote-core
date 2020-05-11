from py3votecore.random_winner import RandomWinner


def test_random_winner():
    input = [
        {"count": 26, "ballot": ["c1", "c2", "c3"]},
        {"count": 20, "ballot": ["c2", "c3", "c1"]},
        {"count": 23, "ballot": ["c3", "c1", "c2"]},
    ]
    output = RandomWinner(input, random_seed=0).as_dict()

    assert output == {
        "candidates": {"c1", "c2", "c3"},
        "winner": "c1",
        'placements': [{'candidates': ['c1']}, {'candidates': ['c3']}, {'candidates': ['c2']}],
    }
