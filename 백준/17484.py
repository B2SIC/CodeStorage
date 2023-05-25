def dfs(x, y, direction, distance):
    if x == N - 1:
        global ans
        ans = min(ans, min(distance[N - 1]))
        return

    for k in range(3):
        if k == direction:
            continue

        nx = x + dxs[k]
        ny = y + dys[k]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        distance[nx][ny] = distance[x][y] + maps[nx][ny]
        dfs(nx, ny, k, distance)


N, M = map(int, input().split())
INT_MAX = int(1e9)
ans = INT_MAX

maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

# 좌하 0, 하 1, 우하 2
dxs = [1, 1, 1]
dys = [-1, 0, 1]

distance = [[INT_MAX] * M for _ in range(N)]
for i in range(M):
    distance[0][i] = maps[0][i]
    dfs(0, i, -1, distance)

print(ans)
