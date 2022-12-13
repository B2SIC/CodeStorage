import sys


input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
num_list = [0] + list(map(int, input().rstrip().split()))

dp = [0] * (n + 1)
dp[1] = num_list[1]

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + num_list[i]

for _ in range(m):
    st, ed = map(int, input().rstrip().split())
    print(dp[ed] - dp[st - 1])
