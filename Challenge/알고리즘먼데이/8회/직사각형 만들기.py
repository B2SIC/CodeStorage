# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import defaultdict

n = int(input())
stick_list = list(map(int, input().split()))

stick_dict = defaultdict(int)
ans = 0

for stick in stick_list:
    stick_dict[stick] += 1

stick_pair = []

for key, value in stick_dict.items():
    if value >= 2:
        for i in range(value // 2):
            stick_pair.append(key)

stick_pair.sort(reverse=True)

for i in range(0, len(stick_pair), 2):
    if i + 1 < len(stick_pair):
        ans += stick_pair[i] * stick_pair[i + 1]

print(ans)
