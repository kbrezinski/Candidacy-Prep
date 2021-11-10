
#     [weight, value]
I = [[4, 8], [4, 7], [6, 14]]
k = 8

def knapRecursive(I, k):
    table = [[None] * (k + 1) for _ in range(len(I))]
    return knapRecursiveAux(I, k, table, len(I) - 1), table

def knapRecursiveAux(I, k, table, hi):

    # dynamic table check
    if table[hi][k] is not None: return table[hi][k]

    ans = None # defaault answer

    # final element
    if hi == 0:
        # too big for sack
        if I[hi][0] > k:
            ans = 0
        # fits
        else:
            ans = I[hi][1]
    else:
        # too big for sack
        if I[hi][0] > k:
            ans = knapRecursiveAux(I, k, table, hi - 1)
        # fits
        else:
            # don't include it
            s1 = knapRecursiveAux(I, k, table, hi - 1)
            # include it
            s2 = I[hi][1] + knapRecursiveAux(I, k - I[hi][0], table, hi - 1)
            ans = max(s1, s2)

    table[hi][k] = ans
    return ans

ans, table = knapRecursive(I, k)
print(ans)
for s in table:
    print(*s)
