from collections import defaultdict


def generator(get_str):
    elem_dict = defaultdict(int)
    for i in range(len(get_str) - 1):
        make_str = (get_str[i] + get_str[i + 1]).lower()

        if make_str.isalpha():
            elem_dict[make_str] += 1
    return elem_dict


def solution(str1, str2):
    answer = 0
    dict_str1 = generator(str1)
    dict_str2 = generator(str2)

    intersection = 0
    union = 0
    for key, value in dict_str1.items():
        if dict_str2.get(key, -1) != -1:
            intersection += min(value, dict_str2[key])
            union += max(value, dict_str2[key])
        else:
            union += value

    for key, value in dict_str2.items():
        if dict_str1.get(key, -1) == -1:
            union += value

    if union != 0:
        answer = (intersection / union) * 65536
    else:
        answer = 65536
    return int(answer)
