'''
1620번 나는야 포켓몬 마스터 이다솜

해시 자료구조를 이용한 값 찾기 문제
'''

import sys


input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

poketmons = dict()
for i in range(1, n + 1):
    poketmons[input().rstrip()] = i

sorted_poketmons = sorted(poketmons.items(), key=lambda x:x[1])

for _ in range(m):
    quiz = input().rstrip()

    if quiz.isdigit():
        print(sorted_poketmons[int(quiz) - 1][0])
    else:
        print(poketmons[quiz])
