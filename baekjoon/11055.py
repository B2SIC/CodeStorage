n = int(input())
num_list = list(map(int, input().split()))

dp = [0] * 1001
for i in range(1, n + 1):
  dp[i] = num_list[i - 1]

for i in range(2, n + 1):
  for j in range(i):
    if num_list[j] < num_list[i - 1]:
      dp[i] = max(dp[i], dp[j + 1] + num_list[i - 1])

print(max(dp))
