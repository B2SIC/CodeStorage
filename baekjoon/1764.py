import sys

n, m = map(int, input().split())

name_dict = dict()
duplicated_list = list()

for _ in range(n):
  name = sys.stdin.readline().rstrip()
  name_dict[name] = 1

for _ in range(m):
  name = sys.stdin.readline().rstrip()

  if name_dict.get(name, -1) == -1:
    name_dict[name] = 1
  else:
    duplicated_list.append(name)

print(len(duplicated_list))
duplicated_list.sort()

for elem in duplicated_list:
  print(elem)
