import sys

input = sys.stdin.readline

p = int(input().rstrip())
for _ in range(p):
    line = list(map(int, input().rstrip().split()))
    test_case_num = line.pop(0)

    foot_step = 0
    sorted_line = []

    for i in range(len(line)):
        if not sorted_line:
            sorted_line.append(line[i])
        else:
            for j in range(len(sorted_line)):
                if sorted_line[j] > line[i]:
                    foot_step += len(sorted_line) - j
                    sorted_line.insert(j, line[i])
                    break
            else:
                sorted_line.append(line[i])

    print(test_case_num, foot_step)
