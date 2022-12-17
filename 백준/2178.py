from collections import deque

import sys


input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = []
dist = [[-1] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

queue = deque()
queue.append((0, 0))
dist[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if graph[nx][ny] and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

print(dist[n - 1][m - 1])
