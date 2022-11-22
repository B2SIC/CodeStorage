import sys
import heapq

n = int(input())
result = 0
hq = []

for i in range(n):
  get_card = int(sys.stdin.readline().strip())
  heapq.heappush(hq, get_card)

if len(hq) == 1:
  result = 0
else:
  while len(hq) > 1:
    x = heapq.heappop(hq)
    y = heapq.heappop(hq)

    result += x + y
    heapq.heappush(hq, x + y)

print(result)
