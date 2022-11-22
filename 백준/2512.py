n = int(input())

budget = list(map(int, input().split()))
max_budget = int(input())

start = 1
end = max(budget)

result = 0
while start <= end:
  mid = (start + end) // 2
  bill = 0

  for bud in budget:
    if bud > mid:
      bill += mid
    else:
      bill += bud

  if bill <= max_budget:
    result = mid
    start = mid + 1
  else:
    end = mid - 1

print(result)
