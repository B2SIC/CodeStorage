from collections import deque

n, m = map(int, input().split())
graph = list()

for _ in range(n):
    graph.append(list(map(int, input().split())))


def bfs(get_graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    safety_zone = 0

    for i in range(n):
        for j in range(m):
            if get_graph[i][j] == 2:
                queue.append((i, j))

                while queue:
                    x, y = queue.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            continue

                        if get_graph[nx][ny] == 1:
                            continue
                        if get_graph[nx][ny] == 0:
                            get_graph[nx][ny] = 2
                            queue.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if get_graph[i][j] == 0:
                safety_zone += 1

    return safety_zone


wall_pos = list()
max_safe = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            wall_pos.append((i, j))

for i in range(len(wall_pos) - 2):
    for j in range(i + 1, len(wall_pos) - 1):
        for k in range(j + 1, len(wall_pos)):
            # 벽 생성
            copy_graph = [item[:] for item in graph]
            x, y = wall_pos[i]
            copy_graph[x][y] = 1

            x, y = wall_pos[j]
            copy_graph[x][y] = 1

            x, y = wall_pos[k]
            copy_graph[x][y] = 1

            result = bfs(copy_graph)

            if max_safe < result:
                max_safe = result

print(max_safe)
