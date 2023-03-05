def solution(arr):
    queue = []

    for num in arr:
        if queue and queue[-1] == num:
            continue
        queue.append(num)
    return queue
