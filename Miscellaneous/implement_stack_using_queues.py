""" https://leetcode.com/problems/implement-stack-using-queues/ """


class MyStack:
    def __init__(self):
        self.queue = []
        self.front = None
        self.rear = None

    def push(self, x: int) -> None:
        self.queue.append(x)
        if self.front == None:
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1

    def pop(self) -> int:
        l = self.rear - self.front
        while True:
            n = self.queue.pop(0)
            self.rear -= 1
            l -= 1
            if l < 0:
                if not self.queue:
                    self.front = None
                    self.rear = None
                return n
            self.queue.append(n)
            self.rear += 1

    def top(self) -> int:
        return self.queue[self.rear]

    def empty(self) -> bool:
        return len(self.queue) == 0
