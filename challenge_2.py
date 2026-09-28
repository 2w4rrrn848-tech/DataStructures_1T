def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    seen = {}  # value -> index
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return (seen[complement], i)
        seen[x] = i
    raise ValueError("no valid pair found")

def two_sum_all_pairs(nums: list[int], target: int) -> list[tuple[int, int]]:
    seen = {}
    pairs = []
    for j, x in enumerate(nums):
        for i in seen.get(target - x, []):
            pairs.append((i, j))
        seen.setdefault(x, []).append(j)
    return pairs


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([3, 2, 4], 6) == (1, 2)
    assert two_sum([-3, 4, 3, 90], 0) == (0, 2)
    assert two_sum([0, 4, 3, 0], 0) == (0, 3)   
    assert two_sum([3, 3], 6) == (0, 1)          

    assert two_sum_all_pairs([2, 7, 11, 15], 9) == [(0, 1)]
    assert two_sum_all_pairs([1, 1, 1], 2) == [(0, 1), (0, 2), (1, 2)]
    assert two_sum_all_pairs([3, 3], 6) == [(0, 1)]
    assert two_sum_all_pairs([1, 2, 3], 10) == []
    print("Challenge 2: all tests passed")
