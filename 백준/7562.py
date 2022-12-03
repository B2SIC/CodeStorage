from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    l = int(input().rstrip())
    sx, sy = map(int, input().rstrip().split())
    ex, ey = map(int, input().rstrip().split())

    visited = [[False] * (l + 1) for _ in range(l + 1)]
    distance = [[0] * (l + 1) for _ in range(l + 1)]

    dx = [-2, -2, 2, 2, -1, 1, -1, 1]
    dy = [-1, 1, -1, 1, -2, -2, 2, 2]

    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = True

    ans = 0
    while queue:
        x, y = queue.popleft()

        if x == ex and y == ey:
            break

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue

            if not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1

    print(distance[ex][ey])
