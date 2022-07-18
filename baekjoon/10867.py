n = int(input())

array = list(map(int, input().split()))

array = sorted(list(set(array)))

for num in array:
  print(num, end=' ')
