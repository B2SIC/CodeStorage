from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().rstrip())))

print(graph)
visited = [[0] * m for _ in range(n)]

queue = deque()
queue.append((0, 0))
visited[0][0] = 1

# 하우상좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while queue:
    x, y = queue.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if not visited[nx][ny] and graph[nx][ny] == 1:
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))

print(visited[n -1][m - 1])
