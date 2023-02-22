import sys

input = sys.stdin.readline

n = int(input().rstrip())
graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))

# 머리 찾기
is_find = False
head_x, head_y = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == "*":
            head_x, head_y = i, j
            is_find = True
            break
    if is_find:
        break

# 심장 위치
heart_x, heart_y = head_x + 1, head_y
print(heart_x + 1, heart_y + 1)

# 왼팔 길이(심장 기준 <-)
left_hand = 0
for i in range(heart_y - 1, -1, -1):
    if graph[heart_x][i] == '*':
        left_hand += 1
    else:
        break
# 오른팔 길이(심장 기준 ->)
right_hand = 0
for i in range(heart_y + 1, n):
    if graph[heart_x][i] == '*':
        right_hand += 1
    else:
        break
# 허리 길이(심장 기준 ↓)
back = 0
back_x, back_y = 0, heart_y
for i in range(heart_x + 1, n):
    if graph[i][heart_y] == '*':
        back += 1
        back_x = i
    else:
        break
# 왼쪽 다리(허리 기준 왼쪽 대각선 길이)
left_leg = 0
cur_x, cur_y = back_x + 1, back_y - 1
while cur_x < n:
    if graph[cur_x][cur_y] == '*':
        left_leg += 1
        cur_x += 1
    else:
        break
# 오른쪽 다리(허리 기준 오른쪽 대각선 길이)
right_leg = 0
cur_x, cur_y = back_x + 1, back_y + 1
while cur_x < n:
    if graph[cur_x][cur_y] == '*':
        right_leg += 1
        cur_x += 1
    else:
        break

print(left_hand, right_hand, back, left_leg, right_leg)
