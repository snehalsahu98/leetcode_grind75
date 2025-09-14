class MyQueue:

    def __init__(self):
        self.ip = []
        self.op = []

    def revert (self):
        while self.ip:
            self.op.append(self.ip.pop())
    def push(self, x: int) -> None:
        while self.op:
            self.ip.append(self.op.pop())
        self.ip.append(x)

    def pop(self) -> int:
        self.revert()
        return self.op.pop()

    def peek(self) -> int:
        self.revert()
        return self.op[-1]

    def empty(self) -> bool:
        if self.ip or self.op:
            return False
        else: return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()