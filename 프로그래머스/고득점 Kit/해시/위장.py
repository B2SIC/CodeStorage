from collections import defaultdict


def solution(clothes):
    answer = 1
    clothes_map = defaultdict(list)

    for cloth in clothes:
        name, cloth_type = cloth
        clothes_map[cloth_type].append(name)

    for key in clothes_map.keys():
        answer *= len(clothes_map[key]) + 1

    return answer - 1
