n = int(input())

dp = [1]

i = 1
num = 0
while num <= 1000000000:
    num = dp[i - 1] + (6 * i)
    dp.append(num)
    i += 1

for j in range(len(dp)):
    if n <= dp[j]:
        print(j + 1)
        break
