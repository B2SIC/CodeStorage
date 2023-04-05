from heapq import heappush, heappop, heapify


def solution(scoville, K):
    answer = 0

    heapify(scoville)

    while True:
        s1 = heappop(scoville)
        if s1 >= K:
            break

        if not scoville:
            answer = -1
            break
        s2 = heappop(scoville)

        heappush(scoville, s1 + (s2 * 2))
        answer += 1

    return answer
