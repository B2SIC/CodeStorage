# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 에라토스테네스의 체를 이용한 풀이
def get_prime(n: int):
    check = [False, False] + [True] * (n - 1)

    for i in range(2, int(n ** 0.5) + 1):
        if check[i]:
            for j in range(i * 2, n + 1, i):
                check[j] = False

    return [i for i in range(2, n + 1) if check[i]]


n = int(input())
get_num_list = list(map(int, input().split()))

prime = get_prime(n)
answer = 0

for i in prime:
    answer += get_num_list[i - 1]

print(answer)
