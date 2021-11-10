
from collections import deque

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data) -> None:
        # check if current node is empty
        if self.data:
            # check if new data should go left
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            # check if new data should go right
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:  # otherwise just add to current node
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def DFS(self):
        stack = deque()

        if self.data:
            stack.append(self.data)

        if self.left is None:
            stack.append()



root = Node(10)
root.insert(15)
root.insert(-2)
root.insert(2)
root.print_tree()
