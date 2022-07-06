import sys

n = int(input())
input_list = list()

for i in range(n):
  get_str = sys.stdin.readline().rstrip()
  input_list.append(get_str)

alpha_dict = dict()
for alpha_str in input_list:
  length = len(alpha_str)

  for alpha in alpha_str:
    if alpha in alpha_dict.keys():
      alpha_dict[alpha] += pow(10, length - 1)
    else:
      alpha_dict[alpha] = pow(10, length - 1)
    length -= 1

idx = 0
value_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for count in sorted(alpha_dict.items(), key=lambda x:x[1], reverse=True):
  alpha_dict[count[0]] = value_list[idx]
  idx += 1

result = 0
for alpha in input_list:
  number = ''
  for idx in alpha:
    number += str(alpha_dict[idx])

  result += int(number)

print(result)
