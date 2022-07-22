from collections import deque

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    array = eval(input())
    result = 0

    queue = deque(array)

    reverse_count = 0
    result = ''
    for order in p:
        if order == "R":
            reverse_count += 1
        elif order == "D":
            if len(queue) > 0:
                if reverse_count % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                result = 'error'

    if result != 'error':
        s = '['

        if reverse_count % 2 == 1:
            queue.reverse()

        for rs in queue:
            s += str(rs) + ','

        if len(queue) == 0:
            s += ']'
        else:
            s = s[:-1] + ']'

        result = s

    print(result)
