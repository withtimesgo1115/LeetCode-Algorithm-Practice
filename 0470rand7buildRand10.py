"""
Implement rand10() using rand7().
LeetCode 470 - Given a method rand7 that generates uniform random integers
in [1, 7], implement a method rand10 that generates uniform random integers
in [1, 10].
"""

import random


def rand7() -> int:
    """Generate a uniform random integer in [1, 7]."""
    return random.randint(1, 7)


def rand10() -> int:
    """Generate a uniform random integer in [1, 10] using only rand7()."""
    # (rand7()-1)*7 + rand7() generates uniform integers in [1, 49]
    num = (rand7() - 1) * 7 + rand7()
    while num > 10:
        num = (rand7() - 1) * 7 + rand7()
    return num
