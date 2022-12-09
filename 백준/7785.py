'''
7785번 회사에 있는 사람

해시 기본 문제
'''

import sys


input = sys.stdin.readline

door_log = dict()
for _ in range(int(input().rstrip())):
    name, status = input().rstrip().split()
    door_log[name] = status

for key, value in sorted(door_log.items(), reverse=True):
    if value == "enter":
        print(key)
