
import heapq
import numpy as np

q = []
sol = []

weightMatrix = {
    key: set() for key in range(8)
}

weights = {
    (4, 5): 20,
    (5, 6): 18,
    (1, 6): 10,
    (1, 7): 12,
    (1, 0): 16,
    (0, 2): 8,
    (0, 3): 14,
    (3, 4): 28,
    (3, 5): 24,
    (2, 5): 6,
    (2, 6): 10,
    (2, 1): 30,
    (1, 3): 28
}

## W = {0: {(1, 20), (5, 14)}}
for key, w in weights.items():
    src, dest = key[0], key[1]
    weightMatrix[src].add((w, dest))
    weightMatrix[dest].add((w, src))

def recursivePrims(i: int = 0):
    ## i = src

    ## item = (weight, dst)
    for item in weightMatrix[i]:
        heapq.heappush(q, item)

    ## extract the smallest weight
    try:
        item = heapq.heappop(q)
        print(item)
    except:
        return None

    weightMatrix[i].discard(item)
    weightMatrix[item[1]].discard((item[0], i))

    sol.append(item)
    recursivePrims(item[1])

recursivePrims(0)

#print(sol)
