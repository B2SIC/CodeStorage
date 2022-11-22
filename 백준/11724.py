from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
ans = 0

for _ in range(m):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

for node in range(1, n + 1):
    if visited[node]:
        continue

    queue = deque()
    queue.append(node)
    visited[node] = True

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if visited[i]: continue
            queue.append(i)
            visited[i] = True
    ans += 1

print(ans)
