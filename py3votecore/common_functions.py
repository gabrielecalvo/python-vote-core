import collections


def matching_keys(dict, target_value):
    return set([key for key, value in dict.items() if value == target_value])


def unique_permutations(xs):
    if len(xs) < 2:
        yield xs
    else:
        h = []
        for x in xs:
            h.append(x)
            if x in h[:-1]:
                continue
            ts = xs[:]
            ts.remove(x)
            for ps in unique_permutations(ts):
                yield [x] + ps


def ensure_listlike(x):
    if isinstance(x, collections.Iterable) and not isinstance(x, str):
        return x
    else:
        return [x]


def get_placement_from_tallies(tallies):
    revdict = collections.defaultdict(list)
    for k, v in tallies.items():
        revdict[v].append(k)

    result = [{'points': k, 'candidates': v} for k, v in revdict.items()]
    result = sorted(result, key=lambda x: x['points'], reverse=True)
    return result


def get_candidates_from_ballots(ballots):
    candidates = set()
    for b in ballots:
        candidates |= set(ensure_listlike(b['ballot']))
    return candidates
