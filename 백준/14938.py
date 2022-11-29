import sys


input = sys.stdin.readline
INF = int(1e18)

n, m, r = map(int, input().rstrip().split())
item_count = [0] + list(map(int, input().rstrip().split()))
graph = [[INF] * (n + 1) for _ in range(n + 1)]
item_graph = [0] * (n + 1)

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().rstrip().split())
    graph[a][b] = l
    graph[b][a] = l

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    item = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            item += item_count[j]
    item_graph[i] = item

print(max(item_graph))
