import sys

n = int(input())

num_dict = dict()
for _ in range(n):
  get_num = int(sys.stdin.readline().rstrip())

  if num_dict.get(get_num, -1) == -1:
    num_dict[get_num] = 1
  else:
    num_dict[get_num] += 1

for num in sorted(num_dict):
  iter = num_dict[num]

  for _ in range(iter):
    print(num)
