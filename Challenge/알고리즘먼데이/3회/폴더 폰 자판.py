# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
s = input()
answer = ''
key_couple = []
key_map = [
    [],
    ['1', '.', ',', '?', '!'],
    ['2', 'A', 'B', 'C'],
    ['3', 'D', 'E', 'F'],
    ['4', 'G', 'H', 'I'],
    ['5', 'J', 'K', 'L'],
    ['6', 'M', 'N', 'O'],
    ['7', 'P', 'Q', 'R', 'S'],
    ['8', 'T', 'U', 'V'],
    ['9', 'W', 'X', 'Y', 'Z']
]

num_str = ''
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        num_str += s[i]
    else:
        num_str += s[i]
        key_couple.append(int(num_str))
        num_str = ''

if num_str != '':
    num_str += s[len(s) - 1]
    key_couple.append(int(num_str))
else:
    key_couple.append(int(s[len(s) - 1]))

for key in key_couple:
    idx = int(str(key)[0])
    target = (len(str(key)) - 1) % len(key_map[int(str(key)[0])])
    answer += key_map[idx][target]

print(answer)
