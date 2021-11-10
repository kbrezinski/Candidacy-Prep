
import numpy as np

def smallest_multiple_of_n_geq_m(n: int, m: int) -> int:
    ## n = 3
    ## m = 25 - 9 = 16
    ##    16 + ((3 - (16 % 3)) % 3)
    return m + ((n - (m % n)) % n)

class PrimeListSieve:
    def __init__(self):
        self._primes: list[int] = [2, 3, 5, 7]
        self.end_segment: int = 1
        self.extend_at_most_n_segments_target: int = 10

    @property
    def primes(self):
        return self._primes

    def _extend_at_most_n_segments(self, n: int) -> None:
        k = self.end_segment
        p, q = self.primes[k], self.primes[k + 1]
        segment = range(p * p, q * q)
        segment_min = min(segment)
        segment_len = len(segment)
        isPrime = [True] * segment_len

        for i in range(k + 1):
            pk = self.primes[i]
            start = smallest_multiple_of_n_geq_m(pk, segment_len)
            is_prime[start - segment_min::pk] = repeat(
            False, len(range(start - segment_min, segment_len, pk)))

        self.primes.extend([x for x, isPrime in zip(segment, isPrime) if isPrime])



    def extend(self) -> None:
        self._extend_at_most_n_segments(self.extend_at_most_n_segments)

s = PrimeListSieve()
