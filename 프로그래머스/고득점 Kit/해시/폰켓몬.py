def solution(nums):
    n = len(nums) // 2
    nums = set(nums)
    return min(n, len(nums))
