import sys

n = int(input())

num_list = list()

for i in range(n):
  get_num = int(sys.stdin.readline().rstrip())
  num_list.append(get_num)

arr_len = len(num_list)
num_dic = dict()

for num in num_list:
  if num_dic.get(num, -1) == -1:
    num_dic[num] = 1
  else:
    num_dic[num] += 1

# 최빈값
max_val_list = list()
max_in_dics = max(num_dic.values())
for key, value in num_dic.items():
  if value == max_in_dics:
    max_val_list.append(key)

if len(max_val_list) > 1:
  max_val_list.sort()
  mode = max_val_list[1]
else:
  mode = max_val_list[0]

print(round(sum(num_list) / arr_len))
print(sorted(num_list)[arr_len // 2])
print(mode)
print(max(num_list) - min(num_list))
