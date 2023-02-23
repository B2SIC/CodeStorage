import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] * m

def dfs(k):
    if k == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return

    for i in range(1, n + 1):
        arr[k] = i
        dfs(k + 1)

dfs(0)
