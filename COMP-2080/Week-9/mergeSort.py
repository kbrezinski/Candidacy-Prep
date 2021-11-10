
import numpy as np

arr = np.random.randint(100, size=10)

def merge_sort(lo: int, hi: int, arr: np.ndarray) -> np.ndarray:

    if lo < hi:
        mid = (lo + hi) // 2
        merge_sort(lo, mid, arr)
        merge_sort(mid + 1, hi, arr)
        merge_sort_aux(lo, mid, hi, arr)

def merge_sort_aux(lo: int, mid: int, hi: int, arr: np.ndarray) -> np.ndarray:

    tmp = np.empty([hi - lo + 1])
    print(tmp.shape)
    k: int = 0

    while (lo < mid + 1 and mid <= hi):
        if (arr[lo] <= arr[mid]):
            tmp[k] = arr[lo]
            lo += 1; k += 1
        else:
            tmp[k] = arr[mid]
            mid += 1; k += 1
    while (lo < mid + 1):
        tmp[k] = arr[lo]
        lo += 1; k += 1
    while (mid <= hi):
        tmp[k] = arr[mid]
        mid += 1; k += 1

    arr

merge_sort(0, len(arr), arr)
