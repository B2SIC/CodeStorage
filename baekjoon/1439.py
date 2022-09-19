s = input()

one_list = list()
zero_list = list()

conn_str = ""
for i in range(0, len(s)):
  if conn_str == "":
    conn_str = s[i]
  elif conn_str[0] == s[i]:
    conn_str += s[i]
  elif conn_str[0] != s[i]:
    if conn_str.startswith('0'):
      zero_list.append(conn_str)
      conn_str = s[i]
    else:
      one_list.append(conn_str)
      conn_str = s[i]

if conn_str.startswith('0'):
  zero_list.append(conn_str)
else:
  one_list.append(conn_str)

print(min(len(one_list), len(zero_list)))
