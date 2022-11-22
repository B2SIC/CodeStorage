n = int(input())
dp = [[0] * 3 for _ in range(n + 1)]
r = [0] * (n + 1)
g = [0] * (n + 1)
b = [0] * (n + 1)

for i in range(1, n + 1):
  r[i], g[i], b[i] = map(int, input().split())

dp[1][0] = r[1]
dp[1][1] = g[1]
dp[1][2] = b[1]

for j in range(2, n + 1):
  dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + r[j]
  dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + g[j]
  dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + b[j]

print(min(dp[n][0], dp[n][1], dp[n][2]))
