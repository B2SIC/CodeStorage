from itertools import permutations
from math import sqrt


def solution(numbers):
    answer = 0

    length = len(numbers)
    make_number = set()
    for i in range(1, length + 1):
        for elem in list(permutations(list(numbers), i)):
            make_number.add(int("".join(elem)))

    for num in make_number:
        if num <= 1:
            continue

        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            answer += 1
    return answer
