n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0
for i in range(n):
    for j in range(n):
        flag = True
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[i][j] <= graph[nx][ny]:
                flag = False
                break

        if flag:
            ans += 1

print(ans)
