from collections import deque

INF = int(1e18)


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[INF] * m for _ in range(n)]

    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if maps[nx][ny] == 1 and visited[x][y] + 1 < visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    if visited[n - 1][m - 1] != INF:
        return visited[n - 1][m - 1]
    return -1