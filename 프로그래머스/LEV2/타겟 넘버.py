count = 0

def dfs(v, numbers, target):
    global count
    if not numbers:
        if v == target:
            count += 1
        return
    dfs(v + numbers[0], numbers[1:], target)
    dfs(v - numbers[0], numbers[1:], target)

def solution(numbers, target):
    global count
    dfs(0, numbers, target)
    return count
