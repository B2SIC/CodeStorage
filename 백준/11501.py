import sys

t = int(input())

for _ in range(t):
  n = int(input())
  prices = list(map(int, sys.stdin.readline().rstrip().split()))
  profit = 0

  max_prices = max(prices)
  max_count = prices.count(max_prices)

  for i in range(len(prices)):
    if prices[i] == max_prices:
      if i != len(prices) - 1:
        if max_count > 1:
          max_count -= 1
        else:
          max_prices = max(prices[i + 1:])
    elif prices[i] < max_prices:
      profit += (max_prices - prices[i])

  print(profit)
