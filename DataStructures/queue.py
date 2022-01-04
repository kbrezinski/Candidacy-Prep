
"""
Implementation of a simple Queue in Python
"""


class Queue:
    def __init__(self, size: int):
        self.maxSize = size
        self._size = 0
        self.queue = [None for _ in range(size)]

    @property
    def size(self):
        print(f"Size is: {self._size}")
        return self._size

    def pop(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            key = self.queue[self._size - 1]
            self._size -= 1
            print(f"Popped item: {key}")

    def push(self, key: int):
        if self._size < self.maxSize:
            self.queue[self._size] = key
            self._size += 1
            print(f"Pushed item: {key}")
        else:
            raise Exception(f"Max Size of {self.maxSize} reached")

    def is_empty(self):
        return self._size == 0


q = Queue(4)

q.is_empty()

q.push(4)
q.push(2)
q.push(-1)
q.push(0)
q.is_empty()

q.size
