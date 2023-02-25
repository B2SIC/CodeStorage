from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))

ans = [[-1] * m for _ in range(n)]

queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            ans[i][j] = 0
            queue.append((i, j))
        elif graph[i][j] == 0:
            ans[i][j] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
while queue:
    x, y = queue.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if graph[nx][ny] == 0:
            continue

        if ans[nx][ny] == -1:
            ans[nx][ny] = ans[x][y] + 1
            queue.append((nx, ny))

for elem in ans:
    print(*elem)
