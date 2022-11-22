def validation(get_str):
    stack = []
    couple_dict = {
        '}': '{',
        ')': '(',
        ']': '['
    }

    for s in get_str:
        if s == '[' or s == '(' or s == '{':
            stack.append(s)
        else:
            if len(stack) == 0:
                return False
            else:
                pop_s = stack.pop()

                if couple_dict[s] != pop_s:
                    return False
    if stack:
        return False

    return True


def solution(s):
    answer = 0

    if validation(s):
        answer += 1

    s_list = list(s)
    for _ in range(1, len(s)):
        s_list.append(s_list.pop(0))
        make_s = "".join(s_list)

        if validation(make_s):
            answer += 1

    return answer
