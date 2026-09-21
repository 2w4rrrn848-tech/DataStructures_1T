class QueueFromStacks:
    def __init__(self):
        self.in_ = []
        self.out = []

    def enqueue(self, x) -> None:
        self.in_.append(x)

    def dequeue(self):
        if not self.out:
            while self.in_:
                self.out.append(self.in_.pop())

        if not self.out:
            raise IndexError("dequeue from empty queue")

        return self.out.pop()


q = QueueFromStacks()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(f"in: {q.in_}")

result = q.dequeue()
print(f"Result: {result}")
print(f"out: {q.out}")