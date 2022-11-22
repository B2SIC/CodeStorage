import sys
import heapq

n, k = map(int, input().split())
answer = 0

jewel = list()
bag = list()

for _ in range(n):
  m, v = map(int, sys.stdin.readline().rstrip().split())
  jewel.append((m, v))

for _ in range(k):
  bag.append(int(sys.stdin.readline().rstrip()))

jewel.sort(key=lambda x: x[0])
bag.sort()

hq = []

idx = 0
for i in range(0, len(bag)):
  while idx < len(jewel) and jewel[idx][0] <= bag[i]:
    heapq.heappush(hq, -jewel[idx][1])
    idx += 1

  if len(hq) >= 1:
    answer += -(heapq.heappop(hq))

print(answer)
