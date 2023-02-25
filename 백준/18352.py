from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)

dist = [-1] * (n + 1)
dist[x] = 0
queue = deque()
queue.append(x)

while queue:
    v = queue.popleft()

    for i in graph[v]:
        if dist[i] == -1:
            dist[i] = dist[v] + 1
            queue.append(i)

if k not in dist:
    print(-1)
else:
    for i in range(1, len(dist)):
        if dist[i] == k:
            print(i)
