import sys

k = int(input())

for i in range(k):
    n, idx = map(int, input().split())
    queue = list(map(int, input().split()))
    count = 0
    max_in_queue = max(queue)

    while len(queue) > 0:
        if queue[0] != max_in_queue:
            queue.append(queue.pop(0))

            if idx == 0:
                idx = len(queue) - 1
            else:
                idx -= 1

        elif idx == 0:
            count += 1
            break
        else:
            queue.pop(0)
            max_in_queue = max(queue)
            count += 1
            idx -= 1

    print(count)
