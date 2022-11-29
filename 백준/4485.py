import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e18)


def dijkstra(n, graph):
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = graph[0][0]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            cost = distance[x][y] + graph[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                queue.append((nx, ny))

    return distance[n - 1][n - 1]


count = 1
while True:
    n = int(input())
    graph = []
    if n:
        for _ in range(n):
            graph.append(list(map(int, input().rstrip().split())))
        ans = dijkstra(n, graph)
        print(f"Problem {count}: {ans}")
        count += 1
    else:
        break
