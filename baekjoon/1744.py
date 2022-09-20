import sys

n = int(input())
answer = 0
num_list = list()

for _ in range(n):
    get_num = int(sys.stdin.readline().rstrip())
    num_list.append(get_num)

if len(num_list) == 1:
    print(num_list[0])
else:
    # 음수 처리
    minus_count = 0
    remove_target = list()
    num_list.sort()
    for i in range(len(num_list)):
        if num_list[i] < 0:
            minus_count += 1

    if minus_count > 0:
        couple = int(minus_count / 2)
        spare = minus_count % 2

        idx = 0
        for _ in range(couple):
            answer += (num_list[idx] * num_list[idx + 1])
            remove_target.append(idx)
            remove_target.append(idx + 1)
            idx += 2

        remove_target.sort(reverse=True)
        for target in remove_target:
            del num_list[target]

        # 0 처리
        if spare == 1:
            zero_count = num_list.count(0)

            if zero_count > 0:
                del num_list[1]
                del num_list[0]

    num_list.sort(reverse=True)

    x_pos = 0
    y_pos = 1
    while x_pos < len(num_list) - 1:
        x = num_list[x_pos]
        y = num_list[y_pos]

        if x + y > x * y:
            answer += (x + y)
        else:
            answer += (x * y)

        x_pos += 2
        y_pos += 2

    if x_pos == len(num_list) - 1:
        answer += num_list[x_pos]

    print(answer)
