import sys
from collections import deque

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[x][y] = 1

    queue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = 0

    for j in range(n):
        for k in range(m):
            if graph[j][k] == 1:
                queue.append((j, k))

                while queue:
                    x, y = queue.popleft()

                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            continue
                        if graph[nx][ny] == 0:
                            continue

                        if graph[nx][ny] == 1:
                            graph[nx][ny] = 0
                            queue.append((nx, ny))

                result += 1

    print(result)
