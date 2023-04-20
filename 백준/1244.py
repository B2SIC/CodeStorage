import sys

input = sys.stdin.readline


def reverse(x):
    if x:
        return 0
    else:
        return 1


n = int(input())
switch = [-1] + list(map(int, input().split()))

p = int(input())
for _ in range(p):
    gender, num = map(int, input().split())

    # 남자의 경우 배수일 때 반전시킴
    if gender == 1:
        for k in range(num, n + 1, num):
            switch[k] = reverse(switch[k])
    elif gender == 2:  # 여자의 경우 대칭 조건 만족 시 반전
        target_s, target_e = num, num  # 대칭 범위
        s, e = num - 1, num + 1
        while s > 0 and e <= n:
            if switch[s] != switch[e]:
                break
            else:
                target_s, target_e = s, e
                s -= 1
                e += 1
        for k in range(target_s, target_e + 1):
            switch[k] = reverse(switch[k])

# 한 줄에 20개씩 출력하기
cnt = 0
while cnt < n:
    cnt += 1
    print(switch[cnt], end=' ')

    if cnt % 20 == 0:
        print()
