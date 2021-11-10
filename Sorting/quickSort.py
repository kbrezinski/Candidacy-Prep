
from random import randrange
from time import perf_counter


def quick_sort(A, first, final, randomize=False):

    if first < final:
        q = partition(A, first, final, randomize=randomize)
        quick_sort(A, first, q - 1, randomize=randomize)
        quick_sort(A, q + 1, final, randomize=randomize)


def partition(A, p, r, randomize=False):

    # add randomize pivot option
    if randomize:
        pivot = randrange(p, r + 1)
        A[pivot], A[r] = A[r], A[pivot]

    # make the final index the comparison
    compare = A[r]

    # first index to check is
    i = p - 1

    # loop from first index up to last one before comparison
    for j in range(p, r):
        # if pivot point is greater than current idx
        if A[j] <= compare:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[r], A[i + 1] = A[i + 1], A[r]
    return i + 1


A = [randrange(-50, 50) for _ in range(2**14)]
B = [randrange(-50, 50) for _ in range(2**14)]

tic = perf_counter()
quick_sort(A, 0, len(A) - 1, randomize=False)
print(f"Time: {perf_counter() - tic:.4f}")

tic = perf_counter()
quick_sort(B, 0, len(A) - 1, randomize=True)
print(f"Random Time: {perf_counter() - tic:.4f}")