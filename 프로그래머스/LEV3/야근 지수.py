import heapq


def solution(n, works):
    if sum(works) <= n:
        return 0

    answer = 0

    works = list(map(lambda x: x * -1, works))
    heapq.heapify(works)
    while n > 0:
        heapq.heappush(works, heapq.heappop(works) + 1)
        n -= 1

    for work in works:
        answer += (work * (-1)) ** 2
    return answer
