# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def search_house(x, y, m, arr):
    # 위쪽 영역
    for k in range(0, m + 1):
        if x - k < 0 or x - k >= n:
            continue
        if arr[x - k][y] == 2:
            return True
        for j in range(1, m - k + 1):
            if 0 <= y - j < n:
                if arr[x - k][y - j] == 2:
                    return True
            if 0 <= y + j < n:
                if arr[x - k][y + j] == 2:
                    return True

    # 아래 영역
    for k in range(1, m + 1):
        if x + k < 0 or x + k >= n:
            continue
        if arr[x + k][y] == 2:
            return True
        for j in range(1, m - k + 1):
            if 0 <= y - j < n:
                if arr[x + k][y - j] == 2:
                    return True
            if 0 <= y + j < n:
                if arr[x + k][y + j] == 2:
                    return True


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

ans_house = 0
for x in range(n):
    for y in range(n):
        if arr[x][y] == 1:
            if search_house(x, y, m, arr):
                ans_house += 1

print(ans_house)
