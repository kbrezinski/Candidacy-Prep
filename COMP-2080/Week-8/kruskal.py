
import heapq
import numpy as np

q = []
sol = []

weightMatrix = {
    key: set() for key in range(8)
}

## (src, dest): weight
weights = { (4, 5): 20, (5, 6): 18, (1, 6): 10, (1, 7): 12,
            (1, 0): 16, (0, 2):  8, (0, 3): 14, (3, 4): 28,
            (3, 5): 24, (2, 5):  6, (2, 6): 10, (2, 1): 30, (1, 3): 28 }

connected = [set() for _ in range(8)]

def is_in_set(src: int, dest: int):
    for item in connected:
        if src, dest in

## Stored as {src: {(weight, dest)}
for key, w in weights.items():
    src, dest = key[0], key[1]
    weightMatrix[src].add((w, dest))
    weightMatrix[dest].add((w, src))
    heapq.heappush(q, (w, src, dest))

## Check if E is N-1
while len(sol) < 8:
    ## (w, src, dest)
    w, src, dest = heapq.heappop(q)
    is_in_set(src, dest)
