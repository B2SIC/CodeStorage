s = input()

s_split_list = list()

while s:
  s_split_list.append(s)
  s = s[1:]

s_split_list.sort()

for item in s_split_list:
  print(item)
