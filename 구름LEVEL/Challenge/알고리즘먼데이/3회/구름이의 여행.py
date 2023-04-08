# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque

n, m, k = map(int, input().split())

graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

# BFS
answer = 0
queue = deque([1])
visited[1] = True

while queue:
    for _ in range(len(queue)):
        v = queue.popleft()

        for i in graph[v]:
            if visited[i] is False:
                queue.append(i)
                visited[i] = True
    answer += 1

    if visited[n] is True:
        break

if k >= answer:
    print("YES")
else:
    print("NO")
