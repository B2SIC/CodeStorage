from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[b].append(a)

ret = [0] * (n + 1)
max_hack_ct = 0

for start in range(1, n + 1):
    queue = deque()
    queue.append(start)

    visited = [False] * (n + 1)
    visited[start] = True

    hack_ct = 0
    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if not visited[i]:
                hack_ct += 1
                visited[i] = True
                queue.append(i)

    if max_hack_ct < hack_ct:
        max_hack_ct = hack_ct

    ret[start] = hack_ct

for i in range(1, n + 1):
    if ret[i] == max_hack_ct:
        print(i, end=' ')
