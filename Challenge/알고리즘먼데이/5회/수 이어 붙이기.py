# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# Unsolved
def concat_number(target):
    x, y = target

    if str(x).endswith(str(y)[0]):
        return int(str(x) + str(y)[1:])
    else:
        return int(str(y) + str(x)[1:])


n = int(input())
num_list = sorted(list(map(int, input().split())), reverse=True)

concat_list = []
for i in range(len(num_list)):
    for j in range(len(num_list)):
        if i == j:
            continue

        if str(num_list[j]).startswith(str(num_list[i])[-1]):
            concat_list.append(sorted([num_list[i], num_list[j]]))

for elem in concat_list:
    x, y = elem

    if x in num_list and y in num_list:
        num_list.append(concat_number(elem))
        num_list[num_list.index(y)] = -1
        num_list[num_list.index(x)] = -1

ans_list = []

for elem in num_list:
    if elem > 0:
        ans_list.append(elem)

ans_list.sort(key=lambda x: str(x)[0])
print("".join(map(str, ans_list)))
