
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
def reverse_list(head):
    prev, curr = None, head
    while curr is not None:
        nxt = curr.next 
        curr.next = prev
        prev, curr = curr, nxt
    return prev
def reverse_list_recursive(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


def build(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


def to_list(head):
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    assert to_list(reverse_list(build([1, 2, 3]))) == [3, 2, 1]
    assert to_list(reverse_list(build([1, 2]))) == [2, 1]
    assert reverse_list(None) is None                       
    assert to_list(reverse_list(build([7]))) == [7]         
    assert to_list(reverse_list_recursive(build([1, 2, 3, 4]))) == [4, 3, 2, 1]
    assert reverse_list_recursive(None) is None
    assert to_list(reverse_list_recursive(build([9]))) == [9]
    print("Challenge 3: all tests passed")
