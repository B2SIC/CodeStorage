n = int(input())

sol_list = list(map(int, input().split()))
sol_list.sort()

start = 0
end = len(sol_list) - 1
min_val = 9999999999
result = (0, 0)
while start < end:
  sum = sol_list[start] + sol_list[end]

  if abs(sum) < min_val:
    min_val = abs(sum)
    result = (sol_list[start], sol_list[end])

  if sum < 0:
    start += 1
  else:
    end -= 1

if result[0] <= result[1]:
  print(result[0], result[1])
else:
  print(result[1], result[0])
