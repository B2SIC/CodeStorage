'''
14501번 퇴사

다이나믹 프로그래밍을 이용한 최대 상담일 계산
'''

import sys


input = sys.stdin.readline

n = int(input().rstrip())

ti = [0]
pi = [0]
for _ in range(n):
    t, p = map(int, input().rstrip().split())
    ti.append(t)
    pi.append(p)

dp = [0] * (n + 1)

if ti[n] > 1:
    dp[n] = 0
else:
    dp[n] = pi[n]

for i in range(n - 1, 0, -1):
    # i에서의 최대치 계산
    pi_max = 0
    if i + ti[i] == n + 1:
        pi_max = pi[i]
    elif i + ti[i] <= n:
        pi_max = pi[i] + dp[i + ti[i]]
    dp[i] = max(dp[i + 1], pi_max)

print(max(dp))
