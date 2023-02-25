from collections import deque
import sys
input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(virus_list, virus_graph):
    queue = deque()
    for virus in virus_list:
        queue.append(virus)

    while queue:
        a, b = queue.popleft()

        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if virus_graph[nx][ny] == 0:
                virus_graph[nx][ny] = 2
                queue.append((nx, ny))
    return virus_graph


n, m = map(int, input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))

# 벽을 세울 수 있는 공간과 시작점 찾기
virus_list = []
find_zero = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            find_zero.append((i, j))
        elif graph[i][j] == 2:
            virus_list.append((i, j))

# 벽 3개 선택하기
safe_zone = 0
select_wall = []
for i in range(len(find_zero)):
    for j in range(i + 1, len(find_zero)):
        for k in range(j + 1, len(find_zero)):
            select_wall.append([find_zero[i], find_zero[j], find_zero[k]])

# 벽 세우고 바이러스 BFS
for wall in select_wall:
    sample_graph = [elem[:] for elem in graph]

    for x, y in wall:
        sample_graph[x][y] = 1

    res = bfs(virus_list, sample_graph)

    calc_safe_zone = 0
    for elem in res:
        calc_safe_zone += elem.count(0)

    if safe_zone < calc_safe_zone:
        safe_zone = calc_safe_zone

print(safe_zone)
