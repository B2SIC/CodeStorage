from collections import deque

n, k = map(int, input().split())
graph = [0 for _ in range(200001)]
visited = [False] * 200001

queue = deque()
queue.append(n)

while queue:
  val = queue.popleft()
  dx = [val - 1, val + 1, val * 2]

  if val == k:
    break

  for i in range(3):
    nval = dx[i]

    if nval < 0 or nval > 100000:
      continue

    if visited[nval] is False:
      graph[nval] = graph[val] + 1
      queue.append(nval)
      visited[nval] = True

print(graph[k])
