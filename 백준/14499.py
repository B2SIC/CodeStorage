n, m, x, y, k = map(int, input().split())
maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))

orders = list(map(int, input().split()))

# 순서: 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dice = [0, 0, 0, 0, 0, 0]

# 동쪽: 1, 서쪽: 2, 북쪽: 3, 남쪽: 4
direction = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]

def roll_dice(d: int):
    global dice
    if d == 1:
        dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]
    elif d == 2:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]
    elif d == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
    elif d == 4:
        dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]

# 명령 실행
for order in orders:
    nx = x + direction[order][0]
    ny = y + direction[order][1]

    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

    x = nx
    y = ny
    roll_dice(order)

    if maps[x][y] == 0:
        maps[x][y] = dice[1]
    else:
        dice[1] = maps[x][y]
        maps[x][y] = 0

    print(dice[0])
