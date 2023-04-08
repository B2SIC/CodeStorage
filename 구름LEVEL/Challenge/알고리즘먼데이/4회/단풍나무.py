# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

days = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while True:
    days_changes = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                continue

            maple_count = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue

                if graph[nx][ny] == 0:
                    maple_count += 1

            if maple_count >= 1:
                days_changes.append([i, j, max(0, graph[i][j] - maple_count)])

    if len(days_changes) == 0:
        break

    for data in days_changes:
        i, j, value = data
        graph[i][j] = value

    days += 1

print(days)
