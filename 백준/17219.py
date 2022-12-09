'''
17219번 비밀번호 찾기

해시를 이용한 값 찾기 문제
'''

import sys


input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

account_data = {}
for _ in range(n):
    site, pw = input().rstrip().split()
    account_data[site] = pw

for _ in range(m):
    print(account_data[input().rstrip()])
