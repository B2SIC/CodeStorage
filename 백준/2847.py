n = int(input())
level_list = list()

for _ in range(n):
  get_level = int(input())
  level_list.append(get_level)

copied_list = list()
copied_list[:] = level_list[::-1]

for i in range(len(copied_list) - 1):
  if copied_list[i] <= copied_list[i + 1]:
    copied_list[i + 1] = copied_list[i] - 1

answer = 0
for k in range(len(level_list)):
  answer += level_list[k] - copied_list[k]

print(answer)
