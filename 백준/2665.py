import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e18)


def dijkstra(n, graph):
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] == 1:
                if distance[x][y] < distance[nx][ny]:
                    distance[nx][ny] = distance[x][y]
                    queue.append((nx, ny))
            elif graph[nx][ny] == 0:
                cost = distance[x][y] + 1
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    queue.append((nx, ny))

    return distance[n - 1][n - 1]


n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

print(dijkstra(n, graph))
