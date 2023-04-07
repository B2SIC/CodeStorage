def dfs(my_cctv, case, visited, r, start, depth):
    if r == depth:
        # CCTV 감시 구역 표시하기
        tmp_maps = [maps[i][:] for i in range(len(maps))]
        for target, order in zip(my_cctv, case):
            for dx, dy in order:
                _, x, y = target
                while True:
                    nx = x + dx
                    ny = y + dy

                    # 범위를 벗어나거나 벽이 있다면 STOP
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        break
                    if tmp_maps[nx][ny] == 6:
                        break

                    if tmp_maps[nx][ny] == 0:
                        tmp_maps[nx][ny] = '#'
                    x, y = nx, ny

        # 사각지대 계산
        global min_res
        res = 0
        for i in range(n):
            for j in range(m):
                if tmp_maps[i][j] == 0:
                    res += 1

        if res < min_res:
            min_res = res
        return

    for i in range(start, len(my_cctv)):
        cctv_num, x, y = my_cctv[i]
        if not visited[i]:
            visited[i] = 1
            for dir in direction[cctv_num]:
                case[depth] = dir
                dfs(my_cctv, case, visited, r, i + 1, depth + 1)
            visited[i] = 0


n, m = map(int, input().split())
min_res = int(1e9)
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

# CCTV 방향 설정
direction = {
    1: [[(0, -1)], [(0, 1)], [(-1, 0)], [(1, 0)]],
    2: [[(0, -1), (0, 1)], [(-1, 0), (1, 0)]],
    3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
    4: [[(-1, 0), (0, 1), (0, -1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]],
    5: [[(-1, 0), (0, 1), (1, 0), (0, -1)]]
}

# CCTV 종류, 위치 얻기
my_cctv = []
for i in range(n):
    for j in range(m):
        if 1 <= maps[i][j] <= 5:
            my_cctv.append((maps[i][j], i, j))

visited = [False] * len(my_cctv)
case = [[] for _ in range(len(my_cctv))]
dfs(my_cctv, case, visited, len(my_cctv), 0, 0)
print(min_res)
