import sys

input = sys.stdin.readline

n = int(input().rstrip())

dp = [0] * (10 ** 6 + 1)
pre = [0] * (10 ** 6 + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    pre[i] = i - 1

    if i % 3 == 0:
        if dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            pre[i] = i // 3
        # dp[i] = min(dp[i], dp[i // 3] + 1)

    if i % 2 == 0:
        if dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            pre[i] = i // 2
        # dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[n])

while n != 1:
    print(n, end=' ')
    n = pre[n]
print(n)
