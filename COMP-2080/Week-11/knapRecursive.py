
#     [weight, value]
I = [[4, 8], [4, 7], [6, 14]]
k = 8

def knapRecursive(I, k):
    return knapRecursiveAux(I, k, len(I) - 1)

def knapRecursiveAux(I, k, hi):

    # final element
    if hi == 0:
        # too big for sack
        if I[hi][0] > k:
            return 0
        # fits
        else:
            return I[hi][1]
    else:
        # too big for sack
        if I[hi][0] > k:
            return knapRecursiveAux(I, k, hi - 1)
        # fits
        else:
            # don't include it
            s1 = knapRecursiveAux(I, k, hi - 1)
            # include it
            s2 = I[hi][1] + knapRecursiveAux(I, k - I[hi][0], hi - 1)
            return max(s1, s2)

print(knapRecursive(I, k))
