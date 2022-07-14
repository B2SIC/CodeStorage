import sys
from collections import deque

n = int(input())

graph = list()

for _ in range(n):
  graph.append(list(map(str, sys.stdin.readline().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
cvd = 0  # 적록색약이 보는 구역 수
non_cvd = 0  # 색약이 없는 사람이 보는 구역 수
cvd_graph = [item[:] for item in graph]

# non_cvd
for i in range(n):
  for j in range(n):
    color = cvd_graph[i][j]

    if color != '-':
      non_cvd += 1
      queue.append((i, j))

    while queue:
      x, y = queue.popleft()

      for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
          continue

        if cvd_graph[nx][ny] == color:
          queue.append((nx, ny))
          cvd_graph[nx][ny] = '-'

# cvd
for i in range(n):
  for j in range(n):
    if graph[i][j] == 'G':
      graph[i][j] = 'R'

for i in range(n):
  for j in range(n):
    color = graph[i][j]

    if color != '-':
      cvd += 1
      queue.append((i, j))

    while queue:
      x, y = queue.popleft()

      for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
          continue

        if graph[nx][ny] == color:
          queue.append((nx, ny))
          graph[nx][ny] = '-'

print(non_cvd, cvd)
