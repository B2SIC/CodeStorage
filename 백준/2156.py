import sys


input = sys.stdin.readline

n = int(input().rstrip())
wine = [0]
for _ in range(n):
    wine.append(int(input().rstrip()))

if n == 1:
    print(wine[n])
else:
    dp = [[0] * 3 for _ in range(n + 1)]
    dp[1][1] = wine[1]
    dp[2][0] = wine[1]  # 2번째 미포함 최대치
    dp[2][1] = wine[2]  # 2번째 포함, 1번째 미포함 최대치
    dp[2][2] = wine[1] + wine[2]  # 2번째 포함, 1번째 포함 최대치

    max_wine = max(wine[1], wine[2], wine[1] + wine[2])
    for i in range(3, n + 1):
        dp[i][0] = max(dp[i - 1])
        dp[i][1] = dp[i - 1][0] + wine[i]
        dp[i][2] = dp[i - 1][1] + wine[i]

        max_wine = max(max_wine, dp[i][0], dp[i][1], dp[i][2])

    print(max_wine)
