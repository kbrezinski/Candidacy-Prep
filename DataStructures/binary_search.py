
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, k: int, node: Node):

        # assign node to root if tree is empty
        if self.root is None:
            self.root = Node(k)
        # if k is smaller than the root
        elif node.left is not None and node.key > k:
            self.insert(k, node.left)
        # if k is larger than the root
        elif node.right is not None and node.key < k:
            self.insert(k, node.right)
        else:


    def in_order_walk(self, node: Node):

        if node is not None:
            self.in_order_walk(node.left)
            print(node.key)
            self.in_order_walk(node.left)


n = BinaryTree()

for i in range(1, 6):
    n.insert(i)

n.in_order_walk(n.root)

