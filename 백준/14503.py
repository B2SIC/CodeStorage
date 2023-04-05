n, m = map(int, input().split())
cur_x, cur_y, d = map(int, input().split())

# 0 = 빈칸, 1 = 벽
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

# 청소 여부 표시
history = [[0] * m for _ in range(n)]

# d = 0(북), 1(동), 2(남), 3(서)
forward = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
backward = {0: (1, 0), 1: (0, -1), 2: (-1, 0), 3: (0, 1)}


def check_valid(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if maps[x][y] == 0:
        return True
    return False


res = 0
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while True:
    # 현재 칸이 청소되지 않았다면 청소
    if maps[cur_x][cur_y] == 0 and history[cur_x][cur_y] == 0:
        history[cur_x][cur_y] = 1
        res += 1

    # 현재 칸 주변 4칸 중 청소 되지 않은 빈칸 찾기
    clean_flag = False
    for dir in direction:
        nx, ny = cur_x + dir[0], cur_y + dir[1]

        # 범위를 벗어나는 경우 제외
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        # 청소 되지 않은 칸이 있다면
        if maps[nx][ny] == 0 and history[nx][ny] == 0:
            clean_flag = True
            break

    if clean_flag:
        # 반시계 방향 90도 회전
        d = (d + 3) % 4

        nx, ny = forward[d]
        # 이동 가능한 칸인지 확인
        if check_valid(cur_x + nx, cur_y + ny):
            # 청소되지 않은 칸이라면
            if history[cur_x + nx][cur_y + ny] == 0:
                cur_x = cur_x + nx
                cur_y = cur_y + ny
    else:
        nx, ny = backward[d]
        # 후진 가능한 칸인지
        if check_valid(cur_x + nx, cur_y + ny):
            # 후진
            cur_x = cur_x + nx
            cur_y = cur_y + ny
        else:
            break

print(res)
