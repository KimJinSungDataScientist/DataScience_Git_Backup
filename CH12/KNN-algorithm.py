from typing import List
from collections import Counter

def raw_majority_vote(labels: List[str]) -> str:
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner

print(raw_majority_vote(['a','b','c','b']))

def majority_vote(labels: List[str]) -> str:
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]

    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count])
    if num_winners == 1:
        return winner
    else:
        return majority_vote(labels[:-1])

assert majority_vote(['a','b','c','b','a']) == 'b'





from typing import NamedTuple
from scratch.linear_algebra import Vector, distance


class LabeledPoint(NamedTuple):
    point: Vector
    label: str


def knn_classify(k: int,
                 labeled_points: List[LabeledPoint],
                 new_point: Vector) -> str:
    by_distance = sorted(labeled_points,
                         key=lambda lp: distance(lp.point, new_point))

    k_nearest_labels = [lp.label for lp in by_distance[:k]]

    return majority_vote(k_nearest_labels)


