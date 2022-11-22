num_box = list()

for n in range(1, 10000):
  while n < 10000:
    n = n + sum(map(int, list(str(n))))

    if n not in num_box:
      num_box.append(n)
    else:
      break

for num in range(1, 10000):
  if num not in num_box:
    print(num)
