import sys

n = int(input())
input_list = list()

for i in range(n):
    r = int(sys.stdin.readline().rstrip())

    if r == 0:
        del input_list[-1]
    else:
        input_list.append(r)

print(sum(input_list))
