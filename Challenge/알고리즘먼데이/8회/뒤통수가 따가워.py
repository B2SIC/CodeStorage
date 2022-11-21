# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# Unsolved(Timeout)
n = int(input())
height_list = list(map(int, input().split()))

dp = [0] * n
dp[1] = 1

if height_list[0] <= height_list[1]:
    max_idx = 1
else:
    max_idx = 0

for i in range(2, len(height_list)):
    if height_list[i - 2] > height_list[i - 1]:
        dp[i] = dp[i - 1] + 1
    else:
        if height_list[i - 1] >= height_list[max_idx]:
            dp[i] = 1
        else:
            check_list = list(reversed(height_list[max_idx:i]))
            ct = 0
            max_num_in_check_list = check_list[0]
            for j in range(1, len(check_list)):
                if max_num_in_check_list < check_list[j]:
                    max_num_in_check_list = check_list[j]
                    ct += 1

            dp[i] = ct + 1

    if height_list[max_idx] <= height_list[i]:
        max_idx = i

print(*dp)

