n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
nxt = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    nxt[a][b] = b

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                nxt[i][j] = nxt[i][k]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

for s in range(1, n + 1):
    for e in range(1, n + 1):
        if nxt[s][e] == 0:
            print(0)
            continue

        path = []
        cur = s
        while cur != e:
            path.append(cur)
            cur = nxt[cur][e]
        path.append(cur)
        print(len(path), end=' ')
        print(" ".join(map(str, path)))
