from collections import deque


n, m = map(int, input().split())
maps = []

# 맵 정보
for _ in range(n):
    maps.append(list(map(int, input().split())))

# 편의점 위치 정보 (입력: 1-indexed, 저장: 0-indexed)
store = [0]  # find idx: 1-indexed
for i in range(m):
    d_x, d_y = map(int, input().split())
    store.append((d_x - 1, d_y - 1))

def is_valid_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

# 우선순위에 따른 방향 설정
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 시뮬레이션
t = 1
res = 0  # 최종 시간 (갱신형)
res_m = []  # 길 찾기 완료한 사람 목록

queue = deque()
maps_by_m = [0]  # 사람별 맵 정보 저장
block = []  # 지나갈 수 없는 좌표 저장
while len(res_m) < m:
    # 지나갈 수 없는 칸 세팅
    block_target = []

    # 1: 편의점을 향해 이동
    for _ in range(len(queue)):
        cur_m, x, y = queue.popleft()
        if cur_m in res_m:
            continue

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if not is_valid_range(nx, ny):
                continue

            if not maps_by_m[cur_m][nx][ny] and (nx, ny) not in block:
                maps_by_m[cur_m][nx][ny] = maps_by_m[cur_m][x][y] + 1
                queue.append((cur_m, nx, ny))
            elif maps_by_m[cur_m][nx][ny] == 777:
                res = t
                res_m.append(cur_m)
                block_target.append((nx, ny))

    # 2: 모두 이동한 뒤에 편의점에 도착한 좌표는 지나갈 수 없도록 세팅
    for target in block_target:
        block.append(target)

    # 3 : 편의점에서 가까운 베이스 캠프 선택하기
    if t <= m:
        base_queue = deque()
        base_queue.append(store[t])
        visited = [[0] * n for _ in range(n)]

        dis = int(1e9)
        min_x, min_y = -1, -1
        while base_queue:
            x, y = base_queue.popleft()

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if not is_valid_range(nx, ny):
                    continue

                if not visited[nx][ny] and (nx, ny) not in block:
                    visited[nx][ny] = visited[x][y] + 1

                    if maps[nx][ny] == 1:
                        if visited[nx][ny] < dis:
                            min_x, min_y = nx, ny
                            dis = visited[nx][ny]
                    else:
                        base_queue.append((nx, ny))

        block.append((min_x, min_y))
        my_map = [[0] * n for _ in range(n)]  # 새로 map 생성
        queue.append((t, min_x, min_y))
        x, y = store[t]
        my_map[x][y] = 777  # 편의점 위치를 777로 설정 (목적지)
        maps_by_m.append(my_map)  # 저장 (목표: 1 -> 2 최단거리 이동)

    t += 1

print(res)
