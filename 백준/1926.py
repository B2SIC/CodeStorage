from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

pic_count = 0
pic_size = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] is False:
            queue.append((i, j))
            visited[i][j] = True

            size = 0
            while queue:
                x, y = queue.popleft()

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue

                    if graph[nx][ny] == 1:
                        if visited[nx][ny] is False:
                            queue.append((nx, ny))
                            visited[nx][ny] = True

                size += 1

            pic_count += 1

            if pic_size < size:
                pic_size = size

print(pic_count)
print(pic_size)
