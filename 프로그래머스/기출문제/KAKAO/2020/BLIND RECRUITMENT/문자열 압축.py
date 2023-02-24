def compress_string(s, split_count):
    res = ''
    if len(s) <= split_count:
        return s

    now_count = 0
    now_string = ''
    split_strings = []
    for elem in s:
        if now_count < split_count:
            now_string += elem
            now_count += 1
        else:
            split_strings.append(now_string)
            now_string = elem
            now_count = 1

    split_strings.append(now_string)

    st, end, count = 0, 0, 0
    while end < len(split_strings):
        if split_strings[st] == split_strings[end]:
            end += 1
            count += 1
        else:
            if count > 1:
                res += str(count) + split_strings[st]
            else:
                res += split_strings[st]
            count = 0
            st = end

    if count > 1:
        res += str(count) + split_strings[st]
    else:
        res += split_strings[st]

    return res


def solution(s):
    answer = len(s)

    for i in range(1, len(s)):
        comp_str = compress_string(s, i)

        if len(comp_str) < answer:
            answer = len(comp_str)
    return answer
