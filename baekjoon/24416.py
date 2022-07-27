n = int(input())

dp_count = 0


def fibonacci_dp(n):
    global dp_count
    dp = [0] * 41
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
        dp_count += 1

    return dp[n]


recurs = fibonacci_dp(n)

print(recurs, dp_count)
