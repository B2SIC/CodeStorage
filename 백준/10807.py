n = int(input())
get_num = list(map(int, input().split()))
find_num = int(input())

num_dict = dict()
for num in get_num:
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

if find_num in num_dict:
    print(num_dict[find_num])
else:
    print(0)
