'''
[TIP]
puddles: 좌표값이 반대인 점에 유의
'''

from collections import deque


def solution(m, n, puddles):
    graph = [[0] * (m + 1) for _ in range(n + 1)]
    for x, y in puddles:
        graph[y][x] = -1

    dx = [0, 1]
    dy = [1, 0]

    queue = deque()
    queue.append([1, 1])
    graph[1][1] = 1

    while queue:
        x, y = queue.popleft()

        if y - 1 >= 1 and graph[x][y - 1] == -1:
            graph[x][y] = graph[x - 1][y]
        elif x - 1 >= 1 and graph[x - 1][y] == -1:
            graph[x][y] = graph[x][y - 1]
        else:
            if y - 1 >= 1 and x - 1 >= 1:
                graph[x][y] = graph[x][y - 1] + graph[x - 1][y]

        for k in range(2):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 1 or ny < 1 or nx > n or ny > m:
                continue

            if graph[nx][ny] == -1:
                continue

            if graph[nx][ny] == 0:
                queue.append([nx, ny])
                graph[nx][ny] = graph[x][y]

    return graph[n][m] % 1000000007
