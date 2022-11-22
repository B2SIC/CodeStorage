from collections import deque
import sys

n = int(input())
match_x, match_y = map(int, input().split())
k = int(input())

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
chk_level = [0] * (n + 1)

for _ in range(k):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  graph[x].append(y)
  graph[y].append(x)

queue = deque([match_x])
visited[match_x] = True

while queue:
  queue_size = len(queue)

  v = queue.popleft()

  for idx in graph[v]:
    if visited[idx] is False:
      queue.append(idx)
      visited[idx] = True
      chk_level[idx] = chk_level[v] + 1

if chk_level[match_y] > 0:
  print(chk_level[match_y])
else:
  print(-1)
