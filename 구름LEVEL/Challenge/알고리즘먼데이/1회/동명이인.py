# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n, my_name = input().split()
n = int(n)
answer = 0

for i in range(n):
    get_name = input()

    if my_name in get_name:
        answer += 1

print(answer)
