
import random


class HashMap:
    def __init__(self, size: int = 9):
        self.maxSize = size
        self.hashMap = [None for _ in range(size)]
        self.p = 101

    def insert(self, K):

        d = {}
        # need to find out which keys resolve to which slots
        # stored as {index: # of occurrences}
        for k in K:
            d[self.h1(k)] = d.get(self.h1(k), 0) + 1

        # create second level hashmap
        for key, val in d.items():
            self.hashMap[key] = [val * val] + list(self.generate_ab()) + [None for _ in range(val * val)]

        # populate with values from dict
        for k in K:
            key = self.h1(k)
            m, a, b = self.hashMap[key][:3]
            mappingIndex = self.h2(k, a, b, m)
            self.hashMap[key][3 + mappingIndex] = k

    def search(self, key):

        idx = self.h1(key)
        m, a, b = self.hashMap[idx][:3]

        if self.hashMap[idx][self.h2(key, a, b, m) + 3] is not None:
            print(f"Found key {key}|{idx} at index {self.h2(key, a, b, m)}")
        else:
            print("KEY NOT FOUND")

    def h1(self, k, a=3, b=42):
        return ((a * k + b) % self.p) % self.maxSize

    def h2(self, k, a, b, m):
        return ((a * k + b) % self.p) % m

    def generate_ab(self):
        # returns a, b where a = (1, p-1), b = (0, p-1)
        return random.choice(range(1, self.p - 1)), random.choice(range(self.p - 1))


K = {10, 22, 37, 40, 52, 60, 70, 72, 75}

mapping = HashMap()
mapping.insert(K)

for k in K:
    mapping.search(k)

print(mapping.hashMap)

