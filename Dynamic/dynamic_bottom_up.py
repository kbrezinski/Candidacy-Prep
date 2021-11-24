
prices = {1: 1, 2: 5, 3: 8, 4: 9, 5: 10,
          6: 17, 7: 17, 8: 20, 9: 24, 10: 30}


def cut_rod(size):
    # loops from a size of 1 to a size of n
    for j in range(1, size + 1):
        q = -1
        for i in range(1, j + 1):
            q = max(q, prices[i] + r[j - i])
        r[j] = q  # stores the largest value so far

    return r[size]


n = 3
r = [None if i > 0 else 0 for i in range(n + 1)]


print(cut_rod(2))
