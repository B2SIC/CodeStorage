def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for i, citation in enumerate(citations):
        if i + 1 >= citation:
            if i + 1 == citation:
                answer = i + 1
            else:
                answer = i
            break

    if answer == 0:
        if min(citations) > len(citations):
            answer = len(citations)

    return answer
