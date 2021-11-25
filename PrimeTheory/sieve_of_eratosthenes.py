
from typing import List
from math import sqrt


def primes_less_than(n: int) -> List[int]:
    if n <= 2:
        return []

    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    # loops from 2 to sqrt of n
    for i in range(2, int(sqrt(n))):

        # check if it hasn't been flagged yet
        if is_prime[i]:
            # in the case of 3, range(3*3, 100, 3) so {9, 12, 15, 18, etc.}
            for x in range(i*i, n, i):
                is_prime[x] = False

    # return the primes that were flagged as True
    return [i for i in range(n) if is_prime[i]]


if __name__ == "__main__":
    import time
    tic = time.perf_counter()
    print(len(primes_less_than(10**9)))
    print(f"Done in {time.perf_counter() - tic:.2f} [s]")

