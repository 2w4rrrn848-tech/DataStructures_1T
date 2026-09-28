PAIRS = {")": "(", "]": "[", "}": "{"}
OPENERS = set(PAIRS.values())

def is_balanced(s: str) -> bool:
    stack = []
    for ch in s:
        if ch in OPENERS:
            stack.append(ch)
        elif ch in PAIRS:
            if not stack or stack.pop() != PAIRS[ch]:
                return False
    return not stack
def first_mismatch_index(s: str) -> int:
    stack = []  # (bracket, index)
    for i, ch in enumerate(s):
        if ch in OPENERS:
            stack.append((ch, i))
        elif ch in PAIRS:
            if not stack or stack.pop()[0] != PAIRS[ch]:
                return i
    return stack[0][1] if stack else -1


if __name__ == "__main__":
    assert is_balanced("(a[b]{c})") is True
    assert is_balanced("([)]") is False
    assert is_balanced("((") is False
    assert is_balanced("") is True
    assert is_balanced(")") is False
    assert is_balanced("(") is False
    assert is_balanced("no brackets here") is True

    assert first_mismatch_index("(a[b]{c})") == -1
    assert first_mismatch_index("([)]") == 2
    assert first_mismatch_index("((") == 0
    assert first_mismatch_index(")") == 0
    print("Challenge 1: all tests passed")
