def dfs(start, depth):
    if depth == m:
        for k in range(1, n + 1):
            if visited[k]:
                print(k, end=' ')
        print()
        return

    for i in range(start, n + 1):
        if not visited[i]:
            visited[i] = 1
            dfs(i + 1, depth + 1)
            visited[i] = 0


n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]
visited = [0] * (n + 1)
dfs(1, 0)