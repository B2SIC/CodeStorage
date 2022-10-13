n = int(input())

dp = [[0] * 2 for _ in range(n + 1)]

for i in range(2, n + 1):
  dp[i][0] = dp[i - 1][0] + 1
  dp[i][1] = i - 1
  if i % 3 == 0:
    if dp[i][0] > dp[i // 3][0] + 1:
      dp[i][0] = dp[i // 3][0] + 1
      dp[i][1] = i // 3
  if i % 2 == 0:
    if dp[i][0] > dp[i // 2][0] + 1:
      dp[i][0] = dp[i // 2][0] + 1
      dp[i][1] = i // 2

print(dp[n][0])

print(n, end=' ')
while n != 1:
  print(dp[n][1], end=' ')
  n = dp[n][1]
