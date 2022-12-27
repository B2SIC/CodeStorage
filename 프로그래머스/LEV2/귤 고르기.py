from collections import Counter


def solution(k, tangerine):
    size_dict = Counter(tangerine)

    i = 0
    chance = len(tangerine) - k
    sorted_size_dict = sorted(size_dict.values())
    while chance > 0:
        if chance >= sorted_size_dict[i]:
            chance -= sorted_size_dict[i]
            i += 1
        else:
            break
    return len(sorted_size_dict[i:])
