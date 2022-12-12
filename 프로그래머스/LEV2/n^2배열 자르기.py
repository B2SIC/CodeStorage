def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        x, y = i // n, i % n

        if y <= x:
            answer.append(x + 1)
        else:
            answer.append(y + 1)
    return answer
