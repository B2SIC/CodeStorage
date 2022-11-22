import math

n, k = map(int, input().split())
answer = []

for i in range(1, int(math.sqrt(n)) + 1):
  if n % i == 0:
    answer.append(i)
    answer.append(n // i)

answer = sorted(list(set(answer)))
if len(answer) < k:
  print(0)
else:
  print(answer[k - 1])
