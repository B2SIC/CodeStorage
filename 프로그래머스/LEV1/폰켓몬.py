from collections import defaultdict


def solution(nums):
    poketmon = defaultdict(int)

    for num in nums:
        poketmon[num] += 1

    return min(len(poketmon.keys()), len(nums) // 2)
