# import sys
#
# sys.stdin = open('in1.txt', 'rt')

n = int(input())
max_money = 0
for i in range(n):
    a, b, c = map(int, input().split())

    if a == b and b == c:
        get_money = 10000 + (a * 1000)
    elif a == b or a == c:
        get_money = 1000 + (a * 100)
    elif b == c:
        get_money = 1000 + (b * 100)
    else:
        get_money = (max(a, b, c)) * 100

    if max_money < get_money:
        max_money = get_money

print(max_money)
