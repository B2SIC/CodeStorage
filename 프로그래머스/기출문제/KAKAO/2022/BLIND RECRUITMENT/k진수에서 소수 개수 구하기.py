from math import sqrt


def convert_to_k(num, k):
    s = ""
    while num != 0:
        s += str(num % k)
        num //= k
    return s[::-1]


def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0

    for num in convert_to_k(n, k).split('0'):
        if num and is_prime(int(num)):
            answer += 1

    return answer
