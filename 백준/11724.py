import sys
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(500001)]
visited = [False] * 500001
max_iter = 0
alone_node = set()
queue = deque()

for _ in range(m):
  u, v = map(int, sys.stdin.readline().rstrip().split())
  graph[u].append(v)
  graph[v].append(u)
  alone_node.add(u)
  alone_node.add(v)

  if max_iter < u:
    max_iter = u
  if max_iter < v:
    max_iter = v

result = 0
for i in range(max_iter):
  for v in graph[i]:
    if visited[v] is False:
      result += 1
      queue.append(v)
      visited[v] = True

      while queue:
        val = queue.popleft()
        for k in graph[val]:
          if visited[k] is False:
            queue.append(k)
            visited[k] = True

print(result + (n - len(alone_node)))
