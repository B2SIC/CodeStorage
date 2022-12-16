'''
7576번 토마토

시작점이 여러 개인 BFS 풀이
시작점을 모두 큐에 넣고 BFS를 돌리면 시작점에 대해서 차례대로 BFS를 돌 수 있다.
즉 BFS를 돌 때 큐에 쌓이는 순서는 반드시 거리 순이 된다.
마지막에 익지 않은 토마토가 있는지 확인하는 과정도 중요하다.
'''

from collections import deque
import sys


input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
graph = []
days = [[-1] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))

queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))
            days[i][j] = 0

while queue:
    x, y = queue.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if graph[nx][ny] == 0 and days[nx][ny] == -1:
            queue.append((nx, ny))
            days[nx][ny] = days[x][y] + 1

ans = 0
impossible = False
for i in range(n):
    for j in range(m):
        if days[i][j] == -1 and graph[i][j] != -1:
            ans = -1
            impossible = True
            break
        elif days[i][j] > ans:
            ans = days[i][j]
    if impossible:
        break

print(ans)
