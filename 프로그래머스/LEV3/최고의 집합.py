def solution(n, s):
    if n > s:
        return [-1]
    if n == 1:
        return [s]

    answer = []
    while s > 0:
        val = s // n
        answer.append(val)
        s -= val
        n -= 1

    return answer
