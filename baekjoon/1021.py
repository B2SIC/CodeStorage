from collections import deque

n, m = map(int, input().split())
pos = list(map(int, input().split()))

queue = deque()
for i in range(n + 1):
    queue.append(0)

for p in pos:
    queue[p] = p

queue.popleft()

count = 0
result = 0
idx = 0
while count != m:
    if queue[0] == pos[idx]:
        queue.popleft()
        idx += 1
        count += 1
    else:
        if queue.index(pos[idx]) <= len(queue) // 2:
            queue.append(queue.popleft())
            result += 1
        else:
            queue.appendleft(queue.pop())
            result += 1

print(result)
