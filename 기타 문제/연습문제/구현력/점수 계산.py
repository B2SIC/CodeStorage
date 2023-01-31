# import sys
#
# sys.stdin = open('in2.txt', 'rt')

n = int(input())
seq = list(map(int, input().split()))

score = 0
cont_score = 0

for prob in seq:
    if prob:
        cont_score += 1
        score += cont_score
    else:
        cont_score = 0

print(score)
