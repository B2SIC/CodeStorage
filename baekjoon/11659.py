import sys

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

dp = [0] * 100001
dp[1] = num_list[0]

for i in range(2, n + 1):
  dp[i] = num_list[i - 1] + dp[i - 1]

for _ in range(m):
  i, j = map(int, sys.stdin.readline().rstrip().split())

  if i == j:
    print(num_list[i - 1])
  elif i == 1:
    print(dp[j])
  else:
    print(dp[j] - dp[i - 1])
