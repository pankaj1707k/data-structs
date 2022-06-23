""" https://leetcode.com/problems/lru-cache/ """


class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}  # map key to node
        self.head = Node(0, 0)  # most recently used = head.next
        self.tail = Node(0, 0)  # least recently used = tail.prev
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = Node(key, self.cache[key].value)
        self.remove(self.cache[key])
        self.insert(node)
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.insert(node)
        if self.capacity < 0:
            self.remove(self.tail.prev)

    def insert(self, node: Node) -> None:
        # insert at head
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        self.cache[node.key] = node
        self.capacity -= 1

    def remove(self, node: Node) -> None:
        pre = node.prev
        nxt = node.next
        pre.next = nxt
        nxt.prev = pre
        del self.cache[node.key]
        del node
        self.capacity += 1
