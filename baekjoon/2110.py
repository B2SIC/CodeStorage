import sys

n, c = map(int, input().split())

houses = list()

for _ in range(n):
  houses.append(int(sys.stdin.readline().rstrip()))

houses.sort()
start = 1
end = houses[n - 1] - houses[0]
result = 0

while start <= end:
  mid = (start + end) // 2

  count = 1
  prev_house = houses[0]
  for i in range(1, n):
    if houses[i] - prev_house >= mid:
      count += 1
      prev_house = houses[i]

  if count >= c:
    result = max(result, mid)
    start = mid + 1
  else:
    end = mid - 1

print(result)
