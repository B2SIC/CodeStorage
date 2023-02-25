from itertools import product


def solution(word):
    standard = ['A', 'E', 'I', 'O', 'U']
    words = []
    for i in range(1, 6):
        for elem in list(product(standard, repeat=i)):
            words.append("".join(elem))
    words.sort()
    return words.index(word) + 1
