'''
6198번 옥상 정원 꾸미기

스택을 활용하여 기준보다 작으면서 오른쪽에 있는 빌딩 개수 구하기
'''

import sys

input = sys.stdin.readline

n = int(input().rstrip())

buildings = []
for _ in range(n):
    buildings.append(int(input().rstrip()))

stack = []
watch = [0] * (n)
for i in range(n):
    while stack and stack[-1][1] <= buildings[i]:
        idx, height = stack.pop()
        watch[idx] = i - idx - 1
    stack.append((i, buildings[i]))

while stack:
    idx, height = stack.pop()
    watch[idx] = (n - 1) - idx

print(sum(watch))
