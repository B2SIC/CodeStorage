# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque
import sys

input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)

visited = [0] * (n + 1)
q = deque()
q.append(k)

while q:
    x = q.popleft()

    for i in graph[x]:
        if visited[i] == 0:
            q.append(i)
            visited[i] += visited[x] + 1

        if i == k:
            break

if visited[k] == 0:
    print(-1)
else:
    print(visited[k])
