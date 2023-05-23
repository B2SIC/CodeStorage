import sys

input = sys.stdin.readline

X = input().rstrip()

num_string = ""
N = len(X)
for i in range(1, (len(X) + 1) * 10):
    num_string += str(i)

find = 0
i = 0
j = 0
while find != len(X):
    if num_string[i] == X[j]:
        find += 1
        j += 1
    i += 1

cur_idx = 0
cur_num = 1
while cur_idx < i:
    cur_idx += len(str(cur_num))
    cur_num += 1
print(cur_num - 1)
