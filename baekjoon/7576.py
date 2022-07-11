import sys
from collections import deque

m, n = map(int, input().split())

graph = list()
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

queue = deque()
max_days = 0
flag = False  # 익지 않은 토마토 존재 여부 판별
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))
        if flag is False:
            if graph[i][j] == 0:
                flag = True

if flag is False:
    print(0)
else:
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == -1 or graph[nx][ny] == 1:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

                if graph[nx][ny] > max_days:
                    max_days = graph[nx][ny]

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                max_days = 0

    print(max_days - 1)
