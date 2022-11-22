n, k = list(map(int, input().split()))

standard_coin = list()
for i in range(n):
  get_coin = int(input())
  standard_coin.append(get_coin)

result = 0
while k != 0:
  for coin in reversed(standard_coin):
    if k - coin >= 0:
      result += k // coin
      k = k % coin
      break

print(result)
