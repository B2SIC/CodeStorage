'''
16165번 걸그룹 마스터 준석이

해시를 이용한 값 찾기 및 해시 정렬
'''

from collections import defaultdict
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

girls_dict = defaultdict(list)
for _ in range(n):
    girls_name = input().rstrip()
    group = int(input().rstrip())

    for _ in range(group):
        girls_dict[girls_name].append(input().rstrip())

for _ in range(m):
    quiz = input().rstrip()
    quiz_type = int(input().rstrip())

    if quiz_type:
        for key, value in girls_dict.items():
            if quiz in value:
                print(key)
    else:
        for value in sorted(girls_dict[quiz]):
            print(value)
