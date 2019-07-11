"""

"""

import math


def primes():
    yield 2
    i = 3
    while True:
        if (math.factorial(i - 1) + 1) % i == 0:
            yield i
        i += 2