
from typing import List
from random import randrange

class Node:
    def __init__(self, key: int):
        self.key = key
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, k: int):

        # create new node, check if linked list is empty
        NewNode = Node(k)
        if self.head is None:
            self.head = NewNode
            return

        # traverse linked list until you reach the end
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = NewNode  # point the final item to a new node

    def print(self) -> List[int]:

        keys = []
        if self.head is not None:
            curr = self.head
            keys.append(curr.key)

            while curr.next is not None:
                keys.append(curr.key)
                curr = curr.next

        return keys


class HashTable:
    def __init__(self, max_len: int):
        self.map = [None for _ in range(max_len)]

    def insert(self, key: int):
        hashed_key = self.h(key)
        if self.map[hashed_key] is None:
            self.map[hashed_key] = LinkedList()

        self.map[hashed_key].insert(key)

    def print(self):
        for i, item in enumerate(self.map):
            if item:
                print(f"{i}: {item.print()}")
            else:
                print(f"{i}: empty")

    @staticmethod
    def h(key: int) -> int:
        return key % 10


table = HashTable(10)

for i in range(10):
    table.insert(randrange(1000))

table.print()
