class _Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class _Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, x):
        self._top = _Node(x, self._top)
        self._size += 1

    def pop(self):
        if self._top is None:
            raise IndexError("pop from empty stack")
        node = self._top
        self._top = node.next
        self._size -= 1
        return node.val

    def is_empty(self):
        return self._top is None

    def __len__(self):
        return self._size


class QueueFromStacks:
    def __init__(self):
        self.in_stack = _Stack()
        self.out_stack = _Stack()

    def enqueue(self, x) -> None:          
        self.in_stack.push(x)

    def dequeue(self):
        if self.out_stack.is_empty():
            if self.in_stack.is_empty():
                raise IndexError("dequeue from empty queue")
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)

if __name__ == "__main__":
    q = QueueFromStacks()
    q.enqueue(1); q.enqueue(2); q.enqueue(3)
    assert q.dequeue() == 1 

    q2 = QueueFromStacks()              
    q2.enqueue(1); q2.enqueue(2)
    assert q2.dequeue() == 1
    q2.enqueue(3)
    assert q2.dequeue() == 2
    assert q2.dequeue() == 3
    assert len(q2) == 0

    q3 = QueueFromStacks()
    for v in range(1, 6):
        q3.enqueue(v)
    assert [q3.dequeue() for _ in range(5)] == [1, 2, 3, 4, 5]

    try:    
        QueueFromStacks().dequeue()
        assert False, "expected IndexError"
    except IndexError:
        pass
    print("Challenge 4: all tests passed")
