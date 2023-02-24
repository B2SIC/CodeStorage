s = input()
alpha_list = []
sum_of_num = 0
for elem in s:
    if elem.isalpha():
        alpha_list.append(elem)
    else:
        sum_of_num += int(elem)

alpha_list.sort()
res = "".join(alpha_list) + str(sum_of_num)
print(res)
