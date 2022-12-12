def solution(progresses, speeds):
    answer = []
    stack = []

    max_days = 0
    for i, j in zip(progresses, speeds):
        days = -((i - 100) // j)

        if stack:
            if max_days >= days:
                stack.append(days)
            else:
                count = 0
                while stack and stack[-1] <= max_days:
                    stack.pop()
                    count += 1
                answer.append(count)

                stack.append(days)
                max_days = days
        else:
            stack.append(days)
            max_days = days

    if stack:
        count = 0
        while stack:
            stack.pop()
            count += 1
        answer.append(count)
    return answer
