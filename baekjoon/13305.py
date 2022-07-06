n = int(input())

road_length = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

total_price = 0

oil_price = oil_price[:-1]
min_oil_price = min(oil_price)
min_oil_price_idx = oil_price.index(min_oil_price)

idx = 0
cur_min = oil_price[0]
for price in oil_price:
  if cur_min > price:
    cur_min = price

  total_price += road_length[idx] * cur_min
  idx += 1

print(total_price)
