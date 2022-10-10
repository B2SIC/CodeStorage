# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
get_str = input()

answer = 1
stack = []
for s in get_str:
	if len(stack) < 1:
		stack.append(s)
	else:
		if stack[-1] == s:
			stack.append(s)
		else:
			while stack:
				stack.pop(0)
			answer += 1
			stack.append(s)

print(answer)
