def dfs(p, depth):
    if depth == m:
        print(*p)
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = 1
            p[depth] = i
            dfs(p, depth + 1)
            visited[i] = 0


n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]
visited = [0] * (n + 1)
p = [0] * m
dfs(p, 0)
