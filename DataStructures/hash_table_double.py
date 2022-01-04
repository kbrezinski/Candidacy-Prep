
import random


class HashMap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.curr_size = 0
        self.hash_map = [None for _ in range(max_size)]

    def insert(self, k):
        assert self.curr_size != self.max_size, "hash map is already full"

        i = 0
        if self.curr_size < self.max_size:
            while True:
                hsh = (self.h1(k) + (i * self.h2(k))) % self.max_size

                if self.hash_map[hsh] is None or self.hash_map[hsh] == -1:
                    self.hash_map[hsh] = k
                    self.curr_size += 1
                    print(f"Inserted {k} into hash map of size: {self.curr_size}/{self.max_size}")
                    print(f"Indexed to position {hsh} at {i=}\n")
                    break
                else:
                    print(f"Skipped position {hsh}")
                    i += 1

    def search(self, k):
        assert self.curr_size != 0, "hash map is empty"

        i = 0
        hsh = self.h1(k)

        while self.hash_map[hsh] is not None or self.hash_map[hsh] != -1:
            i += 1
            hsh = (self.h1(k) + (i * self.h2(k))) % self.max_size

            if self.hash_map[hsh] == k:
                print(f"Found key: {k} at index {hsh}")
                return

        print(f"Key: {k} does not exist in hash map")

    @staticmethod
    def h1(k, m=701):
        return k % m

    @staticmethod
    def h2(k, m=700):
        return 1 + (k % m)


mapping = HashMap(199)

for i in range(50):
    mapping.insert(random.choice(range(1, 1_000)))
    mapping.insert(64)

mapping.search(64)

