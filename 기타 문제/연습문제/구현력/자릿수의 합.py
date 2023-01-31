# import sys
#
# sys.stdin = open('in1.txt', 'rt')

def digit_sum(x):
    return sum(map(int, x))

n = int(input())

num_list = list(map(str, input().split()))
sum_of_num = 0
idx = 0
for i in range(len(num_list)):
    calc_sum = digit_sum(num_list[i])
    if sum_of_num < calc_sum:
        sum_of_num = calc_sum
        idx = i

print(num_list[idx])
