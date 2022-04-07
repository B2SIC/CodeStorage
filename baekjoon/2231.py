def sum_of_number_by_stage(num):
    num_str_list = list(map(int, list(str(num))))
    return sum(num_str_list)

i = 1
answer = 0
found_list = list()
get_num = int(input())

while i != get_num:
    sum_of_num = sum_of_number_by_stage(i)

    if (i + sum_of_num) == get_num:
        answer = i
        break
    else:
        i += 1

print(answer)