'''
4179번 불!

시작점이 두 종류인 BFS에 대한 풀이
이 문제는 지훈이는 불에 영향을 받지만 불은 지훈이에게 영향을 받지 않고 BFS를 돌았다.
하지만 만약 두 종류의 BFS에서 어느 하나가 독립적이지 않고 서로 영향을 준다면 다른 풀이가 필요하다.
'''

from collections import deque
import sys


input = sys.stdin.readline

r, c = map(int, input().rstrip().split())
graph = []
for _ in range(r):
    graph.append(list(input().rstrip()))


def solution(r, c, graph):
    queue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 불의 위치 계산
    fire = [[-1] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'F':
                fire[i][j] = 0
                queue.append((i, j))
                break

    # 불에 대한 BFS
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue

            if fire[nx][ny] >= 0:
                continue

            if graph[nx][ny] != '#':
                fire[nx][ny] = fire[x][y] + 1
                queue.append((nx, ny))

    # 지훈이의 위치 계산
    dist = [[-1] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'J':
                dist[i][j] = 0
                queue.append((i, j))
                break

    # 지훈이에 대한 BFS
    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 범위를 벗어났다는 것은 가장자리에 위치했다는 뜻
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                return dist[x][y] + 1

            # 이미 방문했거나 갈 수 없거나
            if dist[nx][ny] >= 0 or graph[nx][ny] == '#':
                continue

            # 불길이 지훈이 보다 빨리 도달하는 곳은 제외
            if fire[nx][ny] != -1 and fire[nx][ny] <= dist[x][y] + 1:
                continue

            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

    return "IMPOSSIBLE"


ans = solution(r, c, graph)
print(ans)
