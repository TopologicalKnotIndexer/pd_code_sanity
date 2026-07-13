from collections import Counter
from typing import Any


def sanity(pd_code: list[list[int | str]]) -> bool:
    """Return whether *pd_code* has the structural invariants of a PD code."""
    if not isinstance(pd_code, list):
        return False

    labels: list[Any] = []
    label_type: type | None = None
    for crossing in pd_code:
        if not isinstance(crossing, list) or len(crossing) != 4:
            return False
        for label in crossing:
            if isinstance(label, bool) or not isinstance(label, (int, str)):
                return False
            if label_type is None:
                label_type = type(label)
            elif type(label) is not label_type:
                return False
            try:
                hash(label)
            except TypeError:
                return False
            labels.append(label)

    return all(count == 2 for count in Counter(labels).values())
