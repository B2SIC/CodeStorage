def dfs(depth):
    if depth == m:
        print(*p)
        return

    before = -1
    for i in range(len(arr)):
        if arr[i] != before:
            p[depth] = arr[i]
            before = arr[i]
            dfs(depth + 1)


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

p = [0] * m
dfs(0)
