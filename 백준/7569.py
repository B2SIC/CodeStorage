'''
7569번 토마토

7576번 토마토의 3차원 버전
풀이 방법은 비슷하며 3차원 배열을 구성하고 이동 방향을 지정하는 것만 달랐던 문제
3차원 배열 그래프를 구성하는 것이 조금 헷갈렸다.
'''

from collections import deque
import sys


input = sys.stdin.readline

m, n, h = map(int, input().rstrip().split())

graph = [[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        graph[i].append(list(map(int, input().rstrip().split())))


def solution(n, m, h, graph):
    dist = [[[-1] * m for _ in range(n)] for _ in range(h)]

    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    queue = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    dist[i][j][k] = 0
                    queue.append((i, j, k))

    while queue:
        x, y, z = queue.popleft()

        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]

            if nx < 0 or ny < 0 or nz < 0 or nx >= h or ny >= n or nz >= m:
                continue

            if graph[nx][ny][nz] == 0 and dist[nx][ny][nz] == -1:
                dist[nx][ny][nz] = dist[x][y][z] + 1
                queue.append((nx, ny, nz))

    ans = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if dist[i][j][k] == -1 and graph[i][j][k] != -1:
                    return -1
                elif dist[i][j][k] > ans:
                    ans = dist[i][j][k]
    return ans


print(solution(n, m, h, graph))
