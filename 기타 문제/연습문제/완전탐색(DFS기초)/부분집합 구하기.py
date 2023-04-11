def dfs(v):
    if v == n + 1:
        for i in range(1, n + 1):
            if visited[i]:
                print(i, end=' ')
        print()
        return
    else:
        visited[v] = 1
        dfs(v + 1)
        visited[v] = 0
        dfs(v + 1)

n = int(input())
visited = [0] * (n + 1)
dfs(1)
