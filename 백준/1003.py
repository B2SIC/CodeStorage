# [value, zero_count, one_count]
dp = [[0] * 3 for _ in range(40 + 1)]
dp[0] = [0, 1, 0]
dp[1] = [1, 0, 1]

for i in range(2, 41):
  dp[i] = [dp[i - 1][j] + dp[i - 2][j] for j in range(3)]

t = int(input())

for _ in range(t):
  n = int(input())
  print(dp[n][1], dp[n][2])
