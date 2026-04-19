from collections import deque

class Node:
    def __init__(self, key: int, value: int) -> None:
        self.prev = self.nxt = None, None
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(-1, -1), Node(-1, -1)
        self.left.nxt = self.right
        self.right.prev = self.left
        
    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    def insert(self, node: Node) -> None:
        prev, nxt = self.right.prev, self.right
        prev.nxt = nxt.prev = node
        node.prev, node.nxt = prev, nxt


    def get(self, key: int) -> int:
        if (key in self.cache):
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if (key in self.cache):
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if (len(self.cache) > self.capacity):
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]
