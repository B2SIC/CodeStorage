from collections import defaultdict


def solution(clothes):
    answer = 1
    closet = defaultdict(list)

    for value, key in clothes:
        closet[key].append(value)

    for key, value in closet.items():
        answer *= len(closet[key]) + 1

    answer -= 1
    return answer
