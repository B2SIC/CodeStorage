from collections import deque
import sys


input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

parent = [0] * (n + 1)

queue = deque()
queue.append(1)

while queue:
    v = queue.popleft()

    for i in graph[v]:
        if not parent[i] and i != 1:
            parent[i] = v
            queue.append(i)

for val in parent[2:]:
    print(val)
