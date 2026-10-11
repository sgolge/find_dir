"""Disposable Codex Cloud/GitHub integration probe.

This file exists exclusively on the isolated Codex direct-control branch.
No production behavior or secret material is involved.

The pending assignment is to implement the function and prove it through
an independently executed bounded test, if a genuine Codex task starts.
"""

def sum_of_squares(n: int) -> int:
    """Return sum(k*k for k in 1..n) for integer n>=0."""
    raise NotImplementedError("Codex integration probe: not yet implemented")


if __name__ == "__main__":
    assert sum_of_squares(100) == 338350
    print("verified: sum_of_squares(100)=338350")
