import sys


input = sys.stdin.readline

n = int(input().rstrip())

Ai = [0]
Bi = [0]
Ai_to_Bi = [0]
Bi_to_Ai = [0]
for _ in range(1, n):
    a, b, a_to_b, b_to_a = map(int, input().rstrip().split())
    Ai.append(a)
    Bi.append(b)
    Ai_to_Bi.append(a_to_b)
    Bi_to_Ai.append(b_to_a)

a, b = map(int, input().rstrip().split())
Ai.append(a)
Bi.append(b)

dp = [[0] * 2 for _ in range(n + 1)]
dp[1][0] = Ai[1]
dp[1][1] = Bi[1]
for k in range(2, n + 1):
    dp[k][0] = min(dp[k - 1][0], dp[k - 1][1] + Bi_to_Ai[k - 1]) + Ai[k]
    dp[k][1] = min(dp[k - 1][1], dp[k - 1][0] + Ai_to_Bi[k - 1]) + Bi[k]
print(min(dp[n]))
