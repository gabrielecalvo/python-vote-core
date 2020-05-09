from py3votecore.borda_count import BordaCount


def test_BordaCount():
    input = [
        {"count": 26, "ballot": ["c1", "c2", "c3"]},
        {"count": 20, "ballot": ["c2", "c3", "c1"]},
        {"count": 23, "ballot": ["c3", "c1", "c2"]},
    ]
    actual = BordaCount(input).as_dict()

    expected = {
            "candidates": {"c1", "c2", "c3"},
            "winner": "c1",
            "rounds": [
                {"tallies": {"c1": 144.0, "c2": 135.0, "c3": 135.0}, "winner": "c1"},
            ],
        }

    # Run tests
    assert actual == expected
