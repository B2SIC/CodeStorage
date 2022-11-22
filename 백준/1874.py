import sys

n = int(input())
seq = list()
result = list()
pop_list = list()
for _ in range(n):
    seq.append(int(sys.stdin.readline().rstrip()))

current_num = 1
idx = 0
stack = list()
while current_num <= n:
    if current_num == seq[idx]:
        stack.append(current_num)
        result.append('+')
        current_num += 1
        pop_list.append(stack.pop())
        result.append('-')
        idx += 1
    else:
        if current_num < seq[idx]:
            stack.append(current_num)
            result.append('+')
            current_num += 1
        else:
            popped_num = stack.pop()
            pop_list.append(popped_num)
            result.append('-')

            if popped_num == seq[idx]:
                idx += 1
            else:
                result.append('NO')
                break

if len(stack) > 0:
    for i in range(len(stack)):
        popped_num = stack.pop()
        pop_list.append(popped_num)
        result.append('-')

if pop_list == seq:
    for rs in result:
        print(rs)
else:
    print("NO")
