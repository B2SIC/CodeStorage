import sys


input = sys.stdin.readline

n = int(input().rstrip())

stairs = [0]
for i in range(n):
    stairs.append(int(input().rstrip()))

if n == 1:
    print(stairs[n])
elif n == 2:
    print(stairs[1] + stairs[2])
else:
    dp = [[0, 0] for _ in range(n + 1)]
    dp[1][0], dp[1][1] = stairs[1], 0
    dp[2][0] = stairs[2]
    dp[2][1] = stairs[1] + stairs[2]

    for i in range(3, n + 1):
        dp[i][0] = max(dp[i - 2][0], dp[i - 2][1]) + stairs[i]
        dp[i][1] = dp[i - 1][0] + stairs[i]

    print(max(dp[n][0], dp[n][1]))
