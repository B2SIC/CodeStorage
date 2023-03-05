def solution(priorities, location):
    answer = 0

    cnt = 0
    while priorities:
        cur = priorities.pop(0)

        if priorities and cur < max(priorities):
            priorities.append(cur)
        else:
            cnt += 1
            if location == 0:
                answer = cnt
                break

        location -= 1
        if location == -1:
            location = len(priorities) - 1
    return answer
