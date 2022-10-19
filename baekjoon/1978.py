n = int(input())
num_list = list(map(int, input().split()))

for num in num_list:
  if num <= 1:
    n -= 1
    continue
  for i in range(2, num):
    if num % i == 0:
      n -= 1
      break

print(n)