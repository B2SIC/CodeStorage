# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from itertools import permutations

n = int(input())
num_list = list(map(int, input().split()))

ans = int(1e18)

for elem in permutations(num_list, n):
    cur = elem[0]
    for i in range(1, n):
        if cur % 10 == elem[i] // 10:
            cur = cur * 10 + elem[i] % 10
        else:
            cur = cur * 100 + elem[i]
    ans = min(ans, cur)

print(ans)