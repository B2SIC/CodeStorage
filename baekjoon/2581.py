def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

n = int(input())
m = int(input())

prime_list = []
for i in range(n, m + 1):
  if is_prime(i):
    prime_list.append(i)

if prime_list:
  print(sum(prime_list))
  print(min(prime_list))
else:
  print(-1)
