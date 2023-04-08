# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def seven_game(num):
    num_list = []

    while num != 0:
        num_list.append(num % 10)
        num //= 10

    a = 0
    for i in range(0, len(num_list), 2):
        a += num_list[i]

    for j in range(1, len(num_list), 2):
        if num_list[j] != 0:
            a *= num_list[j]

    return a % 10


for _ in range(5):
    print(seven_game(int(input())))
