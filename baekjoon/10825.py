import sys

n = int(input())

score_list = list()
for _ in range(n):
    get_input = sys.stdin.readline().rstrip().split()

    for i in range(1, 4):
        get_input[i] = int(get_input[i])

    score_list.append(get_input)

score_list.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for data in score_list:
    print(data[0])
