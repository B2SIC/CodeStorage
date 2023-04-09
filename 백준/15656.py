def dfs(depth):
    if depth == m:
        print(*p)
        return

    for i in range(len(arr)):
        p[depth] = arr[i]
        dfs(depth + 1)


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
p = [0] * m
dfs(0)
