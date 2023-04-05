def dfs(depth, idx):
    global min_value

    if depth == n // 2:
        start, link = 0, 0

        for i in range(n):
            for j in range(i + 1, n):
                if visited[i] and visited[j]:
                    start += graph[i][j] + graph[j][i]
                elif not visited[i] and not visited[j]:
                    link += graph[i][j] + graph[j][i]
        min_value = min(min_value, abs(start - link))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            dfs(depth + 1, i + 1)
            visited[i] = 0

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

arr = [i for i in range(1, n + 1)]
visited = [0] * n
min_value = int(1e9)

dfs(0, 0)
print(min_value)
