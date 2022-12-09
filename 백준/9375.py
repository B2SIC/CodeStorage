'''
9375번 패션왕 신해빈

해시를 활용하여 조합 계산식을 푸는 문제
'''

from collections import defaultdict
import sys


input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())

    my_closet = defaultdict(list)
    for _ in range(n):
        name, c_type = input().rstrip().split()
        my_closet[c_type].append(name)

    comb = 1
    for key in my_closet.keys():
        comb *= (len(my_closet[key]) + 1)
    print(comb - 1)
