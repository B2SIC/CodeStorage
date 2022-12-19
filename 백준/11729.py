'''
11729번 하노이 탑 이동 순서

코드 자체보다 재귀 함수가 왜 이렇게 구성됐는지를 이해하는 것이 더 중요하다.
[재귀 식]
1. n-1개의 원판을 기동 a에서 기둥 6-a-b로 옮긴다.
2. n번 원판을 기둥 a에서 기둥 b로 옮긴다.
3. n-1개의 원판을 기둥 6-a-b에서 기둥 b로 옮긴다.

[Base Condition]
n = 1 이라면 a -> b
'''

import sys


input = sys.stdin.readline

n = int(input().rstrip())

def hanoi(a, b, n):
    if n == 1:
        print(a, b)
        return

    hanoi(a, 6 - a - b, n - 1)
    print(a, b)
    hanoi(6 - a - b, b, n - 1)

print(2 ** n - 1)
hanoi(1, 3, n)
