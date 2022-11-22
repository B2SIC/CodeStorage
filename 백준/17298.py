n = int(input())
seq = list(map(int, input().split()))

stack = list()

for i in range(len(seq)):
  if len(stack) == 0 or seq[stack[-1]] >= seq[i]:
    stack.append(i)
  else:
    while seq[stack[-1]] < seq[i]:
      idx = stack.pop()
      seq[idx] = seq[i]

      if len(stack) == 0:
        break
    stack.append(i)

for st in stack:
  seq[st] = -1

print(*seq)
