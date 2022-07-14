import sys
n = int(input())

coordinate = list()

for _ in range(n):
  coordinate.append(list(map(int, sys.stdin.readline().rstrip().split())))

coordinate.sort(key=lambda x: (x[0], x[1]))

for x, y in coordinate:
  print(x, y)
