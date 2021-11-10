
class HashTableOpen:

    def __init__(self, max_len: int, method: str = 'Linear'):
        self.map = [None for _ in range(max_len)]
        self.currSize = 0
        self.maxLen = max_len
        self.method = method

    def insert(self, k: int):

        # check if hash table is already full
        assert not self.is_full(), f"Hash Table is full, currently at size {self.currSize}"

        idx = 0
        if self.method == 'Linear':
            while (idx < self.maxLen - 1) and (self.map[idx] is not None):
                idx += 1
            self.map[idx] = k
            self.currSize += 1

    def search(self, k: int):

        # check if hash table is totally empty
        assert self.currSize != 0, f"Hash Table is empty, no key available for search"

        idx = 0
        if self.method == 'Linear':
            while (idx < self.maxLen - 1) and (self.map[idx] is not None):
                if self.map[idx] == k:
                    print(f"Key {k} found at index {idx}")
                    return idx
                idx += 1
            print(f"Key {k} not found")
            return -1

    def delete(self, k: int):

        # searches for the key, if it exists set its value to -1
        if self.search(k) != -1:
            self.map[idx] = -1

    def is_full(self):
        return self.currSize >= self.maxLen

    def __str__(self):
        return self.map


table = HashTableOpen(max_len=10)
table.insert(2)
table.insert(-12)
table.search(0)

print(table.map)

