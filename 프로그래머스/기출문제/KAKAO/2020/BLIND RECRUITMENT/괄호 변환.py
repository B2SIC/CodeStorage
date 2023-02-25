def divide_bracket(s):
    left = 0
    right = 0

    for i in range(len(s)):
        if s[i] == '(':
            right += 1
        else:
            left += 1

        if left == right:
            return [s[:i + 1], s[i + 1:]]
    return [s, '']


def balanced_bracket(s):
    return s.count('(') == s.count(')')


def reverse_bracket(s):
    reversed_str = ''
    for elem in s:
        if elem == '(':
            reversed_str += ')'
        else:
            reversed_str += '('
    return reversed_str


def is_right_bracket(s):
    stack = []

    for elem in s:
        if elem == '(':
            stack.append(elem)
        else:
            if stack:
                stack.pop()
            else:
                return False

    if stack:
        return False
    return True


def convert_bracket(w):
    if w == "":
        return w

    u, v = divide_bracket(w)
    if is_right_bracket(u):
        return u + convert_bracket(v)
    else:
        new_str = '('
        new_str += convert_bracket(v)
        new_str += ')'
        new_str += reverse_bracket(u[1:-1])
        return new_str


def solution(p):
    answer = convert_bracket(p)
    return answer
