# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# Unsolved
n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total_ant_house = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            total_ant_house += 1
            is_food = False

            for mp in range(1, m + 1):
                for k in range(4):
                    nx = i + (dx[k] * mp)
                    ny = j + (dy[k] * mp)

                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue

                    if arr[nx][ny] == 2:
                        is_food = True
                        break

                if is_food is True:
                    break

            if is_food is False:
                arr[i][j] = 0
                total_ant_house -= 1

print(total_ant_house)
