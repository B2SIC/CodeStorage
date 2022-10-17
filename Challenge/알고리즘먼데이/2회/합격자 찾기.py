# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
t = int(input())

for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))

    avg = sum(v) / n
    pass_count = 0
    for score in v:
        if score >= avg:
            pass_count += 1

    print(f"{pass_count}/{n}")
