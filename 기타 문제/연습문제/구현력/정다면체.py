from collections import Counter
# import sys
#
# sys.stdin = open('in1.txt', 'rt')

n, m = map(int, input().split())

comb = []
for i in range(1, n + 1):
    for j in range(1, m + 1):
        comb.append(i + j)

sorted_comb = sorted(Counter(comb).items(), key=lambda x: x[1], reverse=True)
max_num = sorted_comb[0][1]
for key, value in sorted_comb:
    if value == max_num:
        print(key, end=' ')
