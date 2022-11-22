import sys

n = int(input())
arr = list()

for _ in range(n):
  arr.append(int(sys.stdin.readline().rstrip()))

arr.sort()

for item in arr:
  print(item)
