# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = input()
bridge_list = list(map(int, input().split()))

answer = 1

for num in bridge_list:
	answer *= num

print(answer)