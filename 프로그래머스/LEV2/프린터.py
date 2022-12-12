from collections import deque


def solution(priorities, location):
    answer = 0

    first = max(priorities)
    queue = deque([(idx, i) for idx, i in enumerate(priorities)])
    while queue:
        loc, priority = queue.popleft()

        if priority == first:
            answer += 1

            if loc == location:
                break
        elif priority < first:
            queue.append((loc, priority))

        if queue:
            first = max([priority for loc, priority in queue])

    return answer
