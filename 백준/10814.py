import sys

n = int(input())

info_list = list()
for _ in range(n):
  age, name = map(str, sys.stdin.readline().rstrip().split())

  info_list.append([int(age), name])

info_list.sort(key=lambda x: x[0])

for age, name in info_list:
  print(age, name)