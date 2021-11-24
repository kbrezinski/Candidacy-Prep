

prices = {1: 1, 2: 5, 3: 8, 4: 9, 5: 10,
          6: 17, 7: 17, 8: 20, 9: 24, 10: 30}


def cut_rod(n):

    if costs[n - 1] is not None:
        return costs[n - 1]

    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1, n + 1):
            q = max(q, prices[i] + cut_rod(n - i))

    costs[n - 1] = q

    return q


length = 10
costs = [None for _ in range(length)]

print(cut_rod(length))

