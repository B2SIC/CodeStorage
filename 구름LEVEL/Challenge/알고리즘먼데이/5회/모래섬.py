# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

days = 0
while True:
    queue = deque()
    drop = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if nx >= n or ny >= m or nx < 0 or ny < 0:
                        continue

                    if arr[nx][ny] == 0:
                        drop.append((i, j))

    if len(drop) == 0:
        days = -1
        break

    for x, y in drop:
        arr[x][y] = 0

    days += 1

    # Check Separate
    visited = [[False] * m for _ in range(n)]
    sep_ct = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] is False:
                queue.append((i, j))
                visited[i][j] = True

                while queue:
                    x, y = queue.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx >= n or ny >= m or nx < 0 or ny < 0:
                            continue

                        if arr[nx][ny] == 1:
                            if visited[nx][ny] is False:
                                queue.append((nx, ny))
                                visited[nx][ny] = True

                sep_ct += 1

    if sep_ct >= 2:
        break

print(days)