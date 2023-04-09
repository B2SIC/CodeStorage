def dfs(start, depth):
    if depth == m:
        print(*p)
        return

    for i in range(start, n + 1):
        p[depth] = i
        dfs(i, depth + 1)


n, m = map(int, input().split())
p = [0] * m
dfs(1, 0)