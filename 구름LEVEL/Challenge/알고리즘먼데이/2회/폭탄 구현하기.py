# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n, k = map(int, input().split())
graph = [[0] * (n + 1) for i in range(n + 1)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(k):
    bomb_x, bomb_y = map(int, input().split())
    graph[bomb_x][bomb_y] += 1

    for i in range(4):
        nx = bomb_x + dx[i]
        ny = bomb_y + dy[i]

        if nx > n or ny > n or nx < 1 or ny < 1:
            continue

        graph[nx][ny] += 1

answer = 0
for line in graph:
    answer += sum(line)

print(answer)
