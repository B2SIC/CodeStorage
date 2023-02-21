from collections import deque

INF = int(1e18)


def solution(begin, target, words):
    if target not in words:
        return 0

    answer = 0

    queue = deque()
    queue.append((begin, 0))

    steps = [INF] * len(words)

    while queue:
        v, s = queue.popleft()  # word, step

        if v == target:
            answer = s
            break

        for i in range(len(words)):
            diff = 0
            for x, y in zip(v, words[i]):
                if x != y:
                    diff += 1

            if diff == 1 and s + 1 < steps[i]:
                steps[i] = s + 1
                queue.append((words[i], steps[i]))

    return answer
