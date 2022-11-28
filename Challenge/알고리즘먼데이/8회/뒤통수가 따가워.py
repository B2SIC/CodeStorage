# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
heads = list(map(int, input().split()))

stack = []
ans = [0] * n
i = 0

while i < n:
    ans[i] = len(stack)

    if stack:
        if stack[-1] > heads[i]:
            stack.append(heads[i])
        else:
            while stack[-1] <= heads[i]:
                stack.pop()
                if not stack:
                    break
            stack.append(heads[i])
    else:
        stack.append(heads[i])
    i += 1

print(*ans)
