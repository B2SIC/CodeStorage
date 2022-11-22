import heapq

n, m = map(int, input().split())
hq = []
card_list = list(map(int, input().split()))

for card in card_list:
  heapq.heappush(hq, card)

for _ in range(m):
  x = heapq.heappop(hq)
  y = heapq.heappop(hq)

  heapq.heappush(hq, x + y)
  heapq.heappush(hq, x + y)

print(sum(hq))
