from collections import deque

affect = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}


def reverse(direction):  # 방향 뒤집기
    if direction == 1:
        return -1
    elif direction == -1:
        return 1


def rotate(gears, num, direction):
    # direction: 1 (시계 방향), -1 (반시계 방향)
    if direction == 1:
        gears[num].appendleft(gears[num].pop())
    elif direction == -1:
        gears[num].append(gears[num].popleft())
    return gears


def adapt(gears, num, direction, visited):  # 전체 톱니바퀴 상태, 변화를 준 번호, 방향, 움직인 톱니바퀴 현황
    global works
    works.append([num, direction])  # 회전 할 대상과 방향 저장

    for i in affect[num]:
        if not visited[i]:
            if i < num:
                if gears[i][2] != gears[num][6]:
                    visited[i] = 1
                    adapt(gears, i, reverse(direction), visited)
            elif i > num:
                if gears[num][2] != gears[i][6]:
                    visited[i] = 1
                    adapt(gears, i, reverse(direction), visited)


works = []
gears = [[]]
for _ in range(4):
    gears.append(deque(list(map(int, input()))))

k = int(input())  # 회전 횟수
for _ in range(k):
    # 회전 시킨 톱니바퀴 번호, 방향
    num, d = map(int, input().split())
    visited = [0] * 5
    visited[num] = 1
    adapt(gears, num, d, visited)

    # 회전
    for work in works:
        gears = rotate(gears, work[0], work[1])
    works.clear()

res = 0
if gears[1][0] == 1: res += 1
if gears[2][0] == 1: res += 2
if gears[3][0] == 1: res += 4
if gears[4][0] == 1: res += 8

print(res)
