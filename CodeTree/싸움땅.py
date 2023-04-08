n, m, k = map(int, input().split())
# 총에 대한 정보
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

# 클래스를 이용해 객체 형태로 나타내면 더 좋음.
players_pos = [0] * (m + 1)  # 플레이어들의 현재 위치 정보
players_dir = [-1] * (m + 1)  # 플레이어들의 현재 방향 정보
players_ab = [-1] * (m + 1)  # 플레이어들의 고유 능력치
players_gun = [0] * (m + 1)  # 플레이어들의 보유 중인 총의 공격력
players_point = [0] * (m + 1)  # 플레이어들의 획득 점수 (최종 답)

for i in range(1, m + 1):
    x, y, d, s = map(int, input().split())
    players_pos[i] = (x - 1, y - 1)
    players_dir[i] = d
    players_ab[i] = s


def pos_valid(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


def check_other_player(idx, x, y):
    check_pos = (x, y)  # 체크할 위치
    for k in range(1, m + 1):
        if idx == k: continue
        # 플레이어 발견
        if check_pos == players_pos[k]:
            return k
    return -1


def turn_direction(idx):  # 오른쪽으로 90도 회전, 2번 수행시 정반대 방향
    players_dir[idx] = (players_dir[idx] + 1) % 4


# dir: 0 ~ 3 : ↑, →, ↓, ←
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 시뮬레이션
for _ in range(k):  # k번의 라운드 진행
    for i in range(1, m + 1):  # 플레이어 1번부터 m 번까지 Action
        player_x, player_y = players_pos[i]

        # 다음 이동 위치 계산
        nx = player_x + dx[players_dir[i]]
        ny = player_y + dy[players_dir[i]]

        if not pos_valid(nx, ny):
            # 정반대 방향으로 회전
            turn_direction(i)
            turn_direction(i)

            # 다음 위치 계산 (반대 방향은 무조건 존재)
            nx = player_x + dx[players_dir[i]]
            ny = player_y + dy[players_dir[i]]

        # 이동
        player_x, player_y = nx, ny
        players_pos[i] = (player_x, player_y)

        # 이동한 곳에 플레이어 존재 여부 파악
        j = check_other_player(i, player_x, player_y)

        # 싸울 대상이 없는 경우
        if j == -1:
            # 이동한 칸에 주울 총이 있는지 파악
            if type(maps[player_x][player_y]) is list:  # 칸에 총이 여러 개 있거나 리스트 타입일 경우
                for k in range(len(maps[player_x][player_y])):
                    if maps[player_x][player_y][k] > players_gun[i]:
                        maps[player_x][player_y][k], players_gun[i] = players_gun[i], maps[player_x][player_y][k]
            else:  # 총이 하나일 경우
                if maps[player_x][player_y] > players_gun[i]:
                    maps[player_x][player_y], players_gun[i] = players_gun[i], maps[player_x][player_y]
        else:
            # 싸울 대상이 있는 경우 서로의 능력치 계산
            i_attack, j_attack = players_ab[i] + players_gun[i], players_ab[j] + players_gun[j]
            getting_point = abs(i_attack - j_attack)  # 포인트 계산
            winner, loser = -1, -1

            # 승자와 패자 구분
            if i_attack > j_attack:
                winner, loser = i, j
            elif i_attack < j_attack:
                winner, loser = j, i
            elif i_attack == j_attack:
                if players_ab[i] > players_ab[j]:
                    winner, loser = i, j
                else:
                    winner, loser = j, i

            # 승자 포인트 획득
            players_point[winner] += getting_point

            # 패자 총 내려놓기
            if players_gun[loser] != 0:
                if type(maps[player_x][player_y]) is list:
                    maps[player_x][player_y].append(players_gun[loser])
                else:
                    maps[player_x][player_y] = [maps[player_x][player_y], players_gun[loser]]
                players_gun[loser] = 0

            # 패자 기존 방향으로 한 칸 이동
            loser_x, loser_y = players_pos[loser]
            loser_nx, loser_ny = loser_x + dx[players_dir[loser]], loser_y + dy[players_dir[loser]]

            # 기존 방향으로 이동할 수 없는 경우 방향 전환
            while not pos_valid(loser_nx, loser_ny) or check_other_player(loser, loser_nx, loser_ny) != -1:
                turn_direction(loser)  # 오른쪽으로 90도 회전
                loser_nx, loser_ny = loser_x + dx[players_dir[loser]], loser_y + dy[players_dir[loser]]

            # 이동
            players_pos[loser] = (loser_nx, loser_ny)

            # 패자는 새로 이동한 칸에 주울 총이 있는지 파악
            if type(maps[loser_nx][loser_ny]) is list:
                for k in range(len(maps[loser_nx][loser_ny])):
                    if maps[loser_nx][loser_ny][k] > players_gun[loser]:
                        maps[loser_nx][loser_ny][k], players_gun[loser] = players_gun[loser], maps[loser_nx][loser_ny][
                            k]
            else:  # 총이 하나일 경우
                if maps[loser_nx][loser_ny] > players_gun[loser]:
                    maps[loser_nx][loser_ny], players_gun[loser] = players_gun[loser], maps[loser_nx][loser_ny]

            # 승자 총 고르기
            if type(maps[player_x][player_y]) is list:
                for k in range(len(maps[player_x][player_y])):
                    if maps[player_x][player_y][k] > players_gun[winner]:
                        maps[player_x][player_y][k], players_gun[winner] = players_gun[winner], \
                                                                           maps[player_x][player_y][k]
            else:  # 총이 하나일 경우
                if maps[player_x][player_y] > players_gun[winner]:
                    maps[player_x][player_y], players_gun[winner] = players_gun[winner], maps[player_x][player_y]

print(*players_point[1:])
