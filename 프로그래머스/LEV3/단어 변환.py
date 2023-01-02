from collections import deque


def comp_word(w1, w2):
    same_count = 0
    for x, y in zip(w1, w2):
        if x != y:
            same_count += 1

    if same_count == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    answer = 0

    used = []
    used.append(begin)
    queue = deque()
    queue.append([begin, 0])

    while queue:
        word, count = queue.popleft()

        if word == target:
            answer = count
            break

        for next in words:
            if word != next and comp_word(word, next) and next not in used:
                queue.append([next, count + 1])
                used.append(next)

    return answer
