# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start = 1
queue = deque()
queue.append(start)
visited[start] = True

friend = 0

while queue:
    node = queue.popleft()

    for i in graph[node]:
        if visited[i] is False:
            queue.append(i)
            visited[i] = True

    friend += 1

print(friend)