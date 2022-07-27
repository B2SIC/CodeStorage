import sys

n = int(input())
s = [0]
dp = [[0, 0, 0] for _ in range(n + 1)]
for _ in range(n):
    s.append(int(sys.stdin.readline().rstrip()))

if n == 1:
    print(s[1])
else:
    dp[1][1] = s[1]
    dp[1][2] = 0
    dp[2][1] = s[2]
    dp[2][2] = s[1] + s[2]

    for i in range(3, n + 1):
        dp[i][1] = max(dp[i - 2][1], dp[i - 2][2]) + s[i]
        dp[i][2] = dp[i - 1][1] + s[i]

    print(max(dp[n][1], dp[n][2]))
