
import time

text1 = 'ACCGGTCGAGTGCGCAC'
text2 = 'GTCGTTCGGAATGCC'
memoize = True


def common_subsequence(text1, text2, memoize):
    tic = time.perf_counter()

    # create i x j matrix
    if memoize:
        table = [[None] * len(text1)] * len(text2)

    ans = common_subsequence_aux(0, 0, text1, text2,
                                 memoize=table if memoize else None)
    print(f"Time taken: {time.perf_counter() - tic:.4e}")
    return ans


def common_subsequence_aux(i, j, text1, text2, memoize=None):

    ans = 0

    # check base condition
    if i >= len(text1) or j >= len(text2):
        return 0

    if memoize:
        if memoize[i][j] is not None:
            return memoize[i][j]
    else:
        # check if characters match
        if text1[i] == text2[j]:
            ans = 1 + common_subsequence_aux(i+1, j+1, text1, text2)
        # otherwise check both subsequence problems
        else:
            ans = max(common_subsequence_aux(i, j+1, text1, text2),
                      common_subsequence_aux(i+1, j, text1, text2))
    if memoize:
        memoize[i][j] = ans
    return ans


print(common_subsequence(text1, text2, memoize=memoize))


