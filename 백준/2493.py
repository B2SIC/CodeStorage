'''
2493번 탑

자신의 왼쪽 탑들 중 자신의 높이보다 큰 탑을 처음으로 만나는 위치 계산
'''
import sys


input = sys.stdin.readline

n = int(input())
top_list = list(map(int, input().rstrip().split()))

stack = []
for i in range(1, n + 1):
    while stack and stack[-1][1] < top_list[i - 1]:
        stack.pop()

    if stack:
        print(stack[-1][0], end=' ')
    else:
        print(0, end=' ')
    stack.append((i, top_list[i - 1]))
