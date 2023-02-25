from collections import deque
import sys
input = sys.stdin.readline


def change_direction(order: str):
    global direction
    if direction == 0:
        if order == 'L':
            direction = 2
        elif order == 'D':
            direction = 1
    elif direction == 1:
        if order == 'L':
            direction = 0
        elif order == 'D':
            direction = 3
    elif direction == 2:
        if order == 'L':
            direction = 3
        elif order == 'D':
            direction = 0
    elif direction == 3:
        if order == 'L':
            direction = 1
        elif order == 'D':
            direction = 2


n = int(input().rstrip())  # 보드 크기
maps = [[0] * (n + 2) for _ in range(n + 2)]
k = int(input().rstrip())  # 사과
for _ in range(k):
    a, b = map(int, input().rstrip().split())
    maps[a][b] = 4  # 사과 == 4

l = int(input().rstrip())
time_order = []
for _ in range(l):
    sec, get_dir = input().rstrip().split()
    sec = int(sec)
    time_order.append((sec, get_dir))
time_order.sort(key=lambda x: x[0])

direction = 0

# 0: →, 1: ↓, 2: ↑, 3: ←
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

time = 0
snake = deque([(1, 0)])
while True:
    # 다음 위치 계산
    last_x, last_y = snake.popleft()

    if not snake:
        nx = last_x + dx[direction]
        ny = last_y + dy[direction]
    else:
        cur_x, cur_y = snake.pop()
        nx = cur_x + dx[direction]
        ny = cur_y + dy[direction]
        snake.append((cur_x, cur_y))

    # 벽을 만나면 종료
    if nx <= 0 or nx > n or ny <= 0 or ny > n:
        break

    if maps[nx][ny] == 1:
        break

    # print(f"다음 좌표: {nx}, {ny}")
    snake.append((nx, ny))

    if maps[nx][ny] == 4:
        snake.appendleft((last_x, last_y))

    maps[last_x][last_y] = 0
    maps[nx][ny] = 1

    # 방향 변환 정보 적용
    if time_order and time_order[0][0] == time:
        # print(f"{direction} 에서")
        sec, get_dir = time_order.pop(0)
        change_direction(get_dir)
        # print(f"{direction} 으로 변경됨")

    # 디버깅을 위한 출력
    # print(f"CUR TIME: {time}")
    # for m in maps:
    #     print(m)
    # print(snake)
    # print('------------------')

    time += 1

print(f"ANS:{time}")
