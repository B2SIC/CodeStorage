import sys
from collections import deque

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = list()

    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

    # 상하좌우 + 대각이동
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    queue = deque()
    island = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                queue.append((i, j))
                island += 1

                while queue:
                    x, y = queue.popleft()

                    for k in range(len(dx)):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx < 0 or ny < 0 or nx >= h or ny >= w:
                            continue

                        if graph[nx][ny] == 1:
                            queue.append((nx, ny))
                            graph[nx][ny] = 0

    print(island)
