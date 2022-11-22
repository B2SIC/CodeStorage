from collections import deque

n = int(input())
graph = list()
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
max_height = 0

for _ in range(n):
    get_line = list(map(int, input().split()))
    if max(get_line) > max_height:
        max_height = max(get_line)

    graph.append(get_line)

max_safe_zone_count = 0
for height in range(0, max_height):
    queue = deque()
    count = 0
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] > height and visited[i][j] is False:
                queue.append((i, j))
                visited[i][j] = True
                count += 1

                while queue:
                    x, y = queue.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            continue

                        if graph[nx][ny] > height and visited[nx][ny] is False:
                            visited[nx][ny] = True
                            queue.append((nx, ny))

    if max_safe_zone_count < count:
        max_safe_zone_count = count

print(max_safe_zone_count)
