from collections import deque
import sys
input = sys.stdin.readline

graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0] * 5 for _ in range(4)]
queue = deque()
ans = 0
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 0 and not visited[i][j]:
            visited[i][j] = 1
            queue.append((i, j))
            ans += 1

            while queue:
                x, y = queue.popleft()
                print(x, y)

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or ny < 0 or nx >= 4 or ny >= 5:
                        continue

                    if not visited[nx][ny] and graph[nx][ny] == 0:
                        queue.append((nx, ny))
                        visited[nx][ny] = 1

print(f"ans={ans}")
