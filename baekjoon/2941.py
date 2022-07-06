croatia_table = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

get_str = input()
i = 0
count = 0

while i <= len(get_str) - 1:
  if get_str[i:i+2] in croatia_table:
    count += 1
    i += 2
  elif get_str[i:i+3] in croatia_table:
    count += 1
    i += 3
  else:
    count += 1
    i += 1

print(count)
