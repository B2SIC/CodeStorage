def dfs(depth):
    if depth == m:
        print(*p)
        return

    for i in range(1, n + 1):
        p[depth] = i
        dfs(depth + 1)


n, m = map(int, input().split())
p = [0] * m
dfs(0)
