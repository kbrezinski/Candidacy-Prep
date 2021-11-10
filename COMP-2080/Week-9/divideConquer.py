
A = [1, 3, 6, 10, 22, 26, 29]
idx = 3

def sortSorted(A: list, k: int):
    print(sortSortedAux(0, len(A), A, k))

def sortSortedAux(lo: int, hi: int, A: list, k: int):

    result = -1
    mid = (lo + hi) // 2

    ## Check if key is in correct pos
    if k == A[mid]:
        result = mid
    ## Check if key is larger than midpoint; recurse right
    elif (k > A[mid] and hi > lo):
        result = sortSortedAux(mid + 1, hi, A, k)
    elif hi > lo:
        result = sortSortedAux(lo, mid - 1, A, k)
    return result

sortSorted(A, 26)
