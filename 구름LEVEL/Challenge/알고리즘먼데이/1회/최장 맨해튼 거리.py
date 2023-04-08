# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
num_list = list(map(int, input().split()))
num_list.sort(reverse=True)

answer = num_list[0] - num_list[2] + num_list[1] - num_list[3]
print(answer)
