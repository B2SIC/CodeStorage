import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] * m
isused = [0] * (n + 1)

def backtracking(num, k):
    if k == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return

    for i in range(num, n + 1):
        if not isused[i]:
            arr[k] = i
            isused[i] = 1
            backtracking(i + 1, k + 1)
            isused[i] = 0

backtracking(1, 0)
