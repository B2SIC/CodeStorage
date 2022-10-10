# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
t = int(input())

for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))

    cut_line = sum(v) / len(v)
    pass_count = 0
    for score in v:
        if score >= cut_line:
            pass_count += 1

    print(str(pass_count) + "/" + str(n))
