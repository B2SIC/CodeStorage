# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
dp = [[0] * 6 for _ in range(n + 1)]

# init
for k in range(1, 6):
    dp[1][k] = 1

for i in range(2, n + 1):
    dp[i][1] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5]) % 100000007
    dp[i][2] = (dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][4]) % 100000007
    dp[i][3] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4] + dp[i - 1][5]) % 100000007
    dp[i][4] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3]) % 100000007
    dp[i][5] = (dp[i - 1][1] + dp[i - 1][3]) % 100000007

print(sum(dp[n]) % 100000007)
