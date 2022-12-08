'''
2531번 회전초밥

시간 복잡도가 좋지 못한 방법으로 해결
나중에 O(NK)보다 낮은 시간 복잡도로 다시 풀어보자.
'''

import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().rstrip().split())

sushi = []
for _ in range(n):
    sushi.append(int(input().rstrip()))

max_type = 0
for i in range(n):
    pick_sushi = []
    j = i
    for _ in range(k):
        pick_sushi.append(sushi[j])
        j = (j + 1) % n

    pick_sushi.append(c)
    calc_type = len(set(pick_sushi))

    if max_type < calc_type:
        max_type = calc_type

print(max_type)
