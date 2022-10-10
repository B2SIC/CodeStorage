# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


n = int(input())
num_list = list(map(int, input().split()))

answer = 0
prime_list = list()
for i in range(2, n + 1):
    if is_prime(i) is True:
        prime_list.append(i - 1)

for i in prime_list:
    answer += num_list[i]

print(answer)
