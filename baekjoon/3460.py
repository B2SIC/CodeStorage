for _ in range(int(input())):
  n = int(input())

  answer = 0
  while n != 0:
    if n % 2 == 1:
      print(answer, end=' ')
    answer += 1
    n //= 2

  print()
