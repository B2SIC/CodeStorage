from collections import deque

INF = int(1e9)
m, n = map(int, input().split())

graph =[]
distance = [[INF] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for _ in range(n):
    graph.append(list(map(int, input())))

queue = deque()
start = (0, 0)
distance[0][0] = 0
queue.append(start)

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if graph[nx][ny] == 0:
            if distance[x][y] < distance[nx][ny]:
                distance[nx][ny] = distance[x][y]
                queue.append((nx, ny))
        else:
            if distance[x][y] + 1 < distance[nx][ny]:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

print(distance[n - 1][m - 1])
