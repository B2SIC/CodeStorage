from collections import deque


def solution(queue1, queue2):
    answer = 0

    queue1, queue2 = deque(queue1), deque(queue2)
    sum_of_queue1, sum_of_queue2 = sum(queue1), sum(queue2)

    while True:
        if sum_of_queue1 > sum_of_queue2:
            val = queue1.popleft()
            sum_of_queue1 -= val
            sum_of_queue2 += val
            queue2.append(val)
        elif sum_of_queue1 < sum_of_queue2:
            val = queue2.popleft()
            sum_of_queue1 += val
            sum_of_queue2 -= val
            queue1.append(val)
        else:
            break
        answer += 1

        if answer > 600000:  # 최대 길이 반복 횟수
            answer = -1
            break

    return answer
