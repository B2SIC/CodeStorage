from collections import deque
import sys
input = sys.stdin.readline


def dfs(v, graph, visited):
    print(v, end=' ')
    visited[v] = 1

    for i in graph[v]:
        if not visited[i]:
            dfs(i, graph, visited)

def bfs(v, graph, visited):
    queue = deque([v])
    visited[v] = 1

    while queue:
        x = queue.popleft()
        print(x, end=' ')

        for k in graph[x]:
            if not visited[k]:
                visited[k] = 1
                queue.append(k)


n, m, v = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for elem in graph:
    elem.sort()

visited = [0] * (n + 1)
dfs(v, graph, visited)
print()

visited = [0] * (n + 1)
bfs(v, graph, visited)
