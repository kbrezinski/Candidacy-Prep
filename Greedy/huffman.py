
import heapq as hq


class Node:
    def __init__(self, left, right, freq):
        self.left = left
        self.right = right
        self.freq = freq


vocab = [('f', 5), ('e', 9), ('c', 12), ('b', 13), ('d', 16), ('a', 45)]
vocab = [(a, b) for b, a in vocab]
hq.heapify(vocab)

huffman_tree = []

while len(vocab) > 1:
    left = hq.heappop(vocab)
    right = hq.heappop(vocab)

    freq = left[0] + right[0]

    # push onto max-queue (freq, right.char + left.char)
    new = (freq, left[1] + right[1])
    hq.heappush(huffman_tree, new)
    hq.heappush(vocab, new)

for i in huffman_tree:
    print(i)

