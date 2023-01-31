from math import sqrt
# import sys


def reverse(x: int):  # 연산을 통해 계산
    res = 0
    while x > 0:
        res = res * 10 + (x % 10)
        x //= 10
    return res

def is_prime(x: int):
    if x <= 1:
        return False

    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# sys.stdin = open('in1.txt', 'rt')

n = int(input())
num_list = list(map(int, input().split()))

for num in num_list:
    num = reverse(num)
    if is_prime(num):
        print(num, end=' ')
