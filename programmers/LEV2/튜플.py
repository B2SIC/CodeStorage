def solution(s):
    answer = []

    s = eval(s.replace('{', '[').replace('}', ']'))

    s.sort(key=lambda x: len(x))

    for arr in s:
        for num in set(arr) - set(answer):
            answer.append(num)

    return answer
